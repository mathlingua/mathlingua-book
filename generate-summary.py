
from typing import List

import shutil
from pathlib import Path
import os

SRC_NAME = 'src'

class Line:
    def __init__(self, text: str, line_number: int):
        self.text = text
        self.line_number = line_number

class Heading:
    def __init__(self, title: str, count: int):
        self.title = title
        self.count = count

class HeadingStack:
    def __init__(self):
        self.data: List[Heading] = []

    def isEmpty(self) -> bool:
        return len(self.data) == 0

    def push(self, heading: Heading):
        self.data.append(heading)

    def peek(self) -> Heading:
        return self.data[len(self.data) - 1]

    def pop(self) -> Heading:
        return self.data.pop()

    def getPath(self) -> str:
        parts = ['.', SRC_NAME]
        for p in self.data:
            parts.append(p.title.replace(' ', '-'))
        return os.path.sep.join(parts) + '.md'

class LineLexer:
    def __init__(self, text):
        self.lines = text.split('\n')
        self.index = 0

    def hasNext(self) -> bool:
        return self.index < len(self.lines)

    def peek(self) -> Line:
        return Line(
            text = self.lines[self.index],
            line_number = self.index + 1,
        )

    def next(self) -> Line:
        line = self.peek()
        self.index += 1
        return line

    def skipBlankLines(self):
        while self.hasNext() and len(self.peek().text.strip()) == 0:
            self.next()


def getSummary(book: str) -> str:
    Path(SRC_NAME).mkdir(parents=True, exist_ok=False)

    summary = '# Summary\n'
    lines = LineLexer(book)
    stack = HeadingStack()

    while lines.hasNext():
        lines.skipBlankLines()
        if not lines.hasNext():
            return summary

        headingLine = lines.next()
        headingText = headingLine.text

        headingCount = 0
        i = 0
        while i < len(headingText) and headingText[i] == '#':
            i += 1
            headingCount += 1

        headingTitle = headingText[headingCount:].strip()
        heading = Heading(title=headingTitle, count=headingCount)

        while (not stack.isEmpty()) and stack.peek().count >= heading.count:
            stack.pop()

        stack.push(heading)

        if headingCount == 0:
            raise Exception(f'(Line {lines.peek().line_number}): Expected a line that starts with # but found "{lines.peek().text}"')

        if headingCount == 1:
            summary += f'\n{headingText}\n'
            continue

        summaryLine = ''
        for _ in range(1, headingCount-1):
            summaryLine += '  '

        filepath = stack.getPath()
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        text = f'# {headingTitle}\n\n'
        while lines.hasNext() and not lines.peek().text.startswith('#'):
            text += f'{lines.next().text}\n'

        with open(filepath, 'w') as f:
            f.write(text)

        parts = filepath.split(os.path.sep)
        # ignore . and src
        partsWithoutSrc = parts[2:]
        filepathWithoutSrc = os.path.sep.join(partsWithoutSrc)

        summaryLine += f'- [{headingTitle}]({filepathWithoutSrc})'
        summary += f'{summaryLine}\n'

    return summary


def main():
    print('Removing the src directory')
    if os.path.exists(SRC_NAME):
        shutil.rmtree(SRC_NAME)
        os.makedirs(SRC_NAME)
    print('Done\n')

    print('Reading book.md')
    with open('book.md', 'r') as bookFile:
        book = bookFile.read()
        print('Done\n')

        summaryFile = f'{SRC_NAME}/SUMMARY.md'

        print('Generating the summary')
        summary = getSummary(book)
        print('Done\n')

        print('Writing the summary')
        with open(summaryFile, 'w') as summaryFile:
            summaryFile.write(summary)
            print('Done\n')
    
    print('Done generating the book')


main()
