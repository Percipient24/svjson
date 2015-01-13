# svjson

A Sublime plugin for converting SVG rects into an array of JSON objects.

For example, it turns:

```
<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 18.1.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1 Tiny//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11-tiny.dtd">
<svg version="1.1" baseProfile="tiny" id="Layer_2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" width="100px" height="100px" viewBox="0 0 100 100" xml:space="preserve">
<rect id="10-n-6" x="95.638" y="72.071" fill="#FFFFFF" stroke="#ED1C24" stroke-width="0.25" stroke-miterlimit="10" width="4.362" height="7.925"/>
<rect id="10-n-7" x="95.638" y="80.199" fill="#FFFFFF" stroke="#ED1C24" stroke-width="0.25" stroke-miterlimit="10" width="4.362" height="7.925"/>
</svg>
```

into

```
[
  {
    "id" : "10-n-6",
    "x" : "95.638",
    "y" : "72.071",
    "w" : "4.362",
    "h" : "7.925"
  },
  {
    "id" : "10-n-7",
    "x" : "95.638",
    "y" : "80.199",
    "w" : "4.362",
    "h" : "7.925"
  }
] 
```

## Installation

1. [**Install Package Control**](https://sublime.wbond.net/installation): a means for easily adding plugins to SublimeText.
2. **Add Repository**: In Sublime, press Cmd+Shift+P and start typing in the entry field so that *Package Control: Add Repository* comes up. Hit enter, and then paste `https://github.com/Percipient24/svjson` in the field that opens at the bottom of the window.
3. **Install svjson**: In Sublime, press Cmd+Shift+P again, and start typing so that *Package Control: Install Package* comes up. Hit enter, and then start typing `svjson`. When it appears on the list, select it, and look to the bottom of the window for a status message that lets you know it worked!

## Usage

Once installed, have the file you would like to convert open and focused, then simply press `Cmd+Alt+J`.

### Changelog

**v0.0.2** Less crud.
- removes DOCTYPE and <svg> as well

**v0.0.1** A first attempt.
- initial commit of the package files to get things up and running
