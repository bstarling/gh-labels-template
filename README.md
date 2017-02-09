# issue-labels-template

## Background
In an attempt to make [Data For Democracy](https://github.com/Data4Democracy) projects as approachable as possible many of the projects decided to implement a standard GitHub label scheme. To ensure consistent naming and color properties across all projects I created a script that would do this automatically using the GitHub API.

## Usage
```
git clone https://github.com/bstarling/issue-labels-template`
pip install pygithub
cd issue-labels-template
python create_labels.py
```
The script uses a `labels.json` input to generate your labels. You can modify this template to use any name/colors you like. A valid `labels.json` file must be in the same directory prior to running the script.

You will need write access to the repo. I suggest testing this on a dummy repo first.

** Please take the time to read through and understand what this script is doing prior to using. It **DOES** write to your GitHub repo **

Docs for [PyGitHub](http://pygithub.readthedocs.io/en/latest/index.html) and [GitHub API](https://developer.github.com/)


## Issue labels explained
If you are interested in using a similar label scheme. Here are the labels we settled on and a short description of each. See them in GitHub GUI [here](https://github.com/bstarling/gh-issues-template/labels) or [here](https://github.com/Data4Democracy/assemble/issues)

**first-pr:** For first timers only. Issues with this label are meant to be a digestible to help people get up to speed with cloning the repository, making a change and creating a pull request. Please do not claim this issue unless it is your first pull request for this project.

**beginner-friendly:** Good for people new to the project or technology stack used by the project. If you are experienced we encourage you not to claim these issues but instead post in comments offering to mentor a new person.

**documentation:** Request for help with documentation

**help-wanted:** Catch all label soliciting for help.

**status-needs-grooming:** Issue is not fully defined. Either the person who opened the issue is not sure how to proceed or did not have time to complete. Indicates further research will be required to determine best path forward.

**status-in-progress:** Someone is actively working on this issue. Please reach out to the person assigned this issue if you would like to contribute.

**status-dev-ready:** Development task that is fully defined and ready to start.

**status-blocked:** Not ready for development.

**data-viz:** Data visualization task.

**data-collection:** Data collection task.

**modeling:** Data modeling, machine learning task.

**storytelling:** Need help crafting a story. Writing assignment.

**enhancement:** expansion of current functionality. New feature request.

**discussion:** Indicates this issue is a public discussion but may not necessarily have a specific task associated to it.

**questions:** A question to or from the project maintainers.


### Sample Output
```
Enter Git Hub username: bstarling
Password:
Orginization or personal repo? [O]rg/[P]ersonal p
Enter Git Hub repo name: gh-issues-template
{'name': 'beginner-friendly', 'color': '0e8a16'}
{'name': 'bug', 'color': 'ee0701'}
{'name': 'data-collection', 'color': 'fef2c0'}
{'name': 'data-viz', 'color': 'fbca04'}
{'name': 'documentation', 'color': 'd4c5f9'}
{'name': 'enhancement', 'color': '84b6eb'}
{'name': 'first-pr', 'color': 'c2e0c6'}
{'name': 'help wanted', 'color': '128A0C'}
{'name': 'modeling', 'color': 'fbca04'}
{'name': 'proposal', 'color': '0052cc'}
{'name': 'question', 'color': 'f9d0c4'}
{'name': 'status-blocked', 'color': 'd93f0b'}
{'name': 'status-dev-ready', 'color': 'c2e0c6'}
{'name': 'status-in-progress', 'color': 'c2e0c6'}
{'name': 'status-needs-grooming', 'color': 'e99695'}
{'name': 'storytelling', 'color': 'd4c5f9'}
------------------

Label template loaded. Confirm load? [Y]: y
Creating label, set NAME = beginner-friendly, COLOR=0e8a16
bug exists, set COLOR=ee0701
Creating label, set NAME = data-collection, COLOR=fef2c0
Creating label, set NAME = data-viz, COLOR=fbca04
Creating label, set NAME = documentation, COLOR=d4c5f9
enhancement exists, set COLOR=84b6eb
Creating label, set NAME = first-pr, COLOR=c2e0c6
help wanted exists, set COLOR=128A0C
Creating label, set NAME = modeling, COLOR=fbca04
Creating label, set NAME = proposal, COLOR=0052cc
question exists, set COLOR=f9d0c4
Creating label, set NAME = status-blocked, COLOR=d93f0b
Creating label, set NAME = status-dev-ready, COLOR=c2e0c6
Creating label, set NAME = status-in-progress, COLOR=c2e0c6
Creating label, set NAME = status-needs-grooming, COLOR=e99695
Creating label, set NAME = storytelling, COLOR=d4c5f9
Thank you for using my hack, have a nice day!
```
