from test_main import test_add

result = test_add()

html_content = f"""
<html>
  <head><title>Test Report</title></head>
  <body>
    <h1>Test Result: {"✅ Passed" if result else "❌ Failed"}</h1>
  </body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)

print("index.html generated")
