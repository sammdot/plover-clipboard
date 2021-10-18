# Plover Clipboard

[![pypi](https://img.shields.io/pypi/v/plover-clipboard)](https://pypi.org/project/plover-clipboard)
![python](https://img.shields.io/pypi/pyversions/plover-clipboard)
![build](https://github.com/sammdot/plover-clipboard/workflows/build/badge.svg)

Plover plugin for accessing the system clipboard. This provides the
`clipboard_paste` meta, which just outputs the last text contents of the clipboard.
The advantage of using this over the paste keyboard command (Ctrl/Cmd-V) is that
the paste can be undone using the steno undo stroke.

To use, add an outline for this command to your dictionary:

```json
{
  "P-FT": "{:clipboard_paste}"
}
```
