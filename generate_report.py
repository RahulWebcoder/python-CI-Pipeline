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

# ✅ Use encoding='utf-8' to support emoji and special characters
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html generated")
