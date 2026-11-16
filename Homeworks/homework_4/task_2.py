dirty = '  "  {  привет   мир  }  "  '

title = dirty.strip()

for ch in ['"', "'", '{', '}', '[', ']']:
    title = title.replace(ch, '')

title = ' '.join(title.split())

words = title.split()
title = ' '.join(word.capitalize() for word in words)

print(title)