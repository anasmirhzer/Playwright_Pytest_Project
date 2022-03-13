# TestAutomation_PlaywrightPytestProject

# Run test in parallel and generate report 
 pytest -n4  --template=html1/index.html --report=test_reports/report.html
 
# Run only regression tests in parallel and generate report 
 pytest -m regression -n4  --template=html1/index.html --report=test_reports/regression_report.html
 
# Run specific test in headed mode 
 pytest -k test_homepage_menu  --headed
 
# Run specific test in parallel in firefox and webkit using 2 CPU
 pytest -k test_homepage_menu -n2  --headed  --browser=firefox --browser webkit

# Run specific test in parallel in firefox and chromium in slow motion 
 pytest -k test_homepage_menu  --headed  --browser=firefox --browser=chromium  --slowmo=500

# Run specific test in slow motion for iphone 11 
 pytest -k test_homepage_menu --headed   --slowmo=500  --device="iPhone 11" 

# Run specific test in slow motion for iphone 11 
 pytest -k test_homepage_menu --headed   --slowmo=500  --device="iPhone 11" 
# Run specific test with video capturing : on/ off / retain-on-failure'
pytest -k test_homepage_menu --video=retain-on-failure

# Run regression test in parallel in firefox, webkit and chromium / headless mode / generate regression report
pytest -m regression -n6  --browser=firefox --browser=webkit  --browser=chromium  --template=html1/index.html --report=test_reports/regression_report.html  --video=retain-on-failure  --env=LOCAL

# Run test with baseurl = local (http://127.0.0.1:8081)
pytest -k test_homepage_menu --base-url http://localhost:8081

# Run test in a specific environment: LOCAL | PROD: default 
pytest -k test_homepage_menu --headed --env=LOCAL
