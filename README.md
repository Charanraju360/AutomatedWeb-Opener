```markdown
# Automated Website Opener 🌐🚀

## Overview
This **Python script** allows users to open multiple websites automatically in their default browser. It takes user input for the number of websites and their URLs, then launches them using Python's `webbrowser` module.

## How It Works
1. The user enters the number of websites they want to open.
2. The script collects the URLs from the user.
3. It then launches all entered websites automatically in the browser.

## Technologies Used
- **Python** 🐍
- **`webbrowser` Module** – Used to open URLs in a browser

## Setup Instructions
1. **Install Python** (if not already installed) from [python.org](https://www.python.org/).
2. **Update the script**:
   - Replace `'C:/YOUR/BROWSER/PATH/BROWSER_NAME.exe %s'` with the correct path to your browser executable.
3. **Run the script**:
   ```bash
   python website_opener.py
   ```

## Example Usage
```
Enter The Number Of Websites That You Want To Open: 3
Enter The Website URL(s):
https://www.google.com
https://www.github.com
https://www.python.org
```
After providing inputs, all three websites will open automatically in the browser.

## Future Improvements
- Add validation to check if URLs are entered correctly 🛠️
- Allow users to save commonly used URLs for quick access 💾
- Enable opening URLs in different browsers 🔄

---

Happy browsing! 🚀✨
