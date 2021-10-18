import pyperclip

def paste(ctx, _):
  pasted = pyperclip.paste()
  if pasted:
    a = ctx.new_action()
    a.text = pasted
    return a
  return ctx.copy_last_action()
