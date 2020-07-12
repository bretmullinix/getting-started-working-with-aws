#!/usr/bin/python
import ansiblelint;
import markdownlint;
import yamllint;
from output_lint import OutputLint


def main():
    ansible_output = ansiblelint.get_ansible_output()
    print(ansible_output)
    markdown_output = markdownlint.get_markdown_output()
    print(markdown_output)
    yamllint_output = yamllint.get_yamllint_output()
    print(yamllint_output)

if __name__ == '__main__':
    main()
