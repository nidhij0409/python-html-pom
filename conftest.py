import pytest
import os
import base64
from lib import create_driver

@pytest.fixture(scope="function")
def get_driver(request):
    driver = create_driver()
    yield driver
    driver.quit()
    # request.addfinalizer(driver.quit)
    # return driver
#------------------------------------------------pytest report----------------------------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs.get("get_driver")
        if driver:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            status = "PASS" if report.passed else "FAIL"
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}_{status}.png")
            driver.save_screenshot(screenshot_path)

            # Embed screenshot as base64 → no external file dependency
            with open(screenshot_path, "rb") as f:
                image_bytes = f.read()
                encoded_image = base64.b64encode(image_bytes).decode("utf-8")

            extra = getattr(report, "extras", [])
            extra.append(pytest_html.extras.html(
                f'<img src="data:image/png;base64,{encoded_image}" '
                f'alt="screenshot" style="width:400px;height:240px;" '
                f'onclick="window.open(this.src)" align="right"/>'
            ))
            report.extras = extra

def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")


#------------------------------------------------charts visual----------------------------------------------------

# Store test results
results_summary = {"passed": 0, "failed": 0, "skipped": 0}

def pytest_runtest_logreport(report):
    if report.when == 'call':
        if report.passed:
            results_summary["passed"] += 1
        elif report.failed:
            results_summary["failed"] += 1
        elif report.skipped:
            results_summary["skipped"] += 1

def pytest_html_results_summary(prefix, summary, postfix):
    # Injecting chart canvas in the HTML report
    prefix.extend([
        '<h2>Test Summary Pie Chart</h2>',
        '<div style="width: 30%; max-width: 600px; margin: auto;"><canvas id="pieChart""></canvas></div>',
        '<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>',
        f'''
        <script>
        const ctx = document.getElementById('pieChart').getContext('2d');
        new Chart(ctx, {{
            type: 'pie',
            data: {{
                labels: ['Passed', 'Failed', 'Skipped'],
                datasets: [{{
                    label: 'Test Results',
                    data: [{results_summary["passed"]}, {results_summary["failed"]}, {results_summary["skipped"]}],
                    backgroundColor: ['#28a745', '#dc3545', '#ffc107'],
                    borderWidth: 1
                }}]
            }},
            options: {{
                responsive: true,
                plugins: {{
                    legend: {{
                        position: 'bottom',
                    }},
                    title: {{
                        display: true,
                        text: 'Pytest Results Overview'
                    }}
                }}
            }}
        }});
        </script>
        '''
    ])
#------------------------------------------allure reports--------------------------------------------

# import allure
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # Execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()

#     # Only add screenshot for actual test calls (not setup/teardown)
#     if rep.when == "call":
#         driver = item.funcargs.get("get_driver")   # assuming your WebDriver fixture is named "setup"
#         if driver:
#             if rep.failed:
#                 # Attach screenshot on failure
#                 allure.attach(driver.get_screenshot_as_png(),
#                               name="Failed Screenshot",
#                               attachment_type=allure.attachment_type.PNG)
#             elif rep.passed:
#                 # Attach screenshot on success
#                 allure.attach(driver.get_screenshot_as_png(),
#                               name="Passed Screenshot",
#                               attachment_type=allure.attachment_type.PNG)