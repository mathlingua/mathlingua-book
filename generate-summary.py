
import shutil
from pathlib import Path

SRC_NAME = 'src'

class LineLexer:
    def __init__(self, text):
        self.lines = text.split('\n')
        self.index = 0

    def hasNext(self) -> bool:
        return self.index < len(self.lines)

    def peek(self) -> str:
        return self.lines[self.index]

    def next(self) -> str:
        line = self.peek()
        self.index += 1
        return line

    def skipBlankLines(self):
        while self.hasNext() and len(self.peek().strip()) == 0:
            self.next()


def getSummary(book: str) -> str:
    Path(SRC_NAME).mkdir(parents=True, exist_ok=False)

    summary = '# Summary\n'
    lines = LineLexer(book)
    while lines.hasNext():
        lines.skipBlankLines()
        if not lines.hasNext():
            return summary

        heading = lines.next()

        headingCount = 0
        i = 0
        while i < len(heading) and heading[i] == '#':
            i += 1
            headingCount += 1

        if headingCount == 0:
            raise Exception(f'Expected a line that starts with # but found {lines.peek()}')

        if headingCount == 1:
            summary += f'\n{heading}\n'
            continue

        summaryLine = ''
        for _ in range(1, headingCount-1):
            summaryLine += '  '

        headingTitle = heading[headingCount:].strip()
        filename = headingTitle.replace(' ', '-').lower() + '.md'
        filepath = f'./{SRC_NAME}/{filename}'

        text = f'# {headingTitle}\n\n'
        while lines.hasNext() and not lines.peek().startswith('#'):
            text += f'{lines.next()}\n'

        with open(filepath, 'w') as f:
            f.write(text)

        summaryLine += f'- [{headingTitle}](./{filename})'
        summary += f'{summaryLine}\n'

    return summary


def main():
    print('Removing the src directory')
    shutil.rmtree(SRC_NAME)
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
