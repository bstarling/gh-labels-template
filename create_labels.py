import getpass
from github import Github
import json


def update_labels():

    while True:
        # loop until authenticated username/pw is entered
        user = input('Enter Git Hub username: ')
        pw = getpass.getpass()

        g = Github(user, pw)
        try:
            g.get_user(user)
            break
        except Exception as e:
            print(e)

    while True:
        # loop until valid org/repository is entered
        org_repo = input('Organization or personal repo? [O]rg/[P]ersonal ')
        if org_repo.lower() not in ['o', 'p']:
            print('Invalid selection --{}--'.format(org_repo))
        elif org_repo.lower() == 'o':
            org_name = input('Organization Name: ')
            try:
                org = g.get_organization(org_name)
                repo_name = input('Enter Git Hub repo name: ')
                repo = org.get_repo(repo_name)
                break
            except Exception as e:
                print(e)
        else:
            try:
                repo_name = input('Enter Git Hub repo name: ')
                repo = g.get_user().get_repo(repo_name)
                break
            except Exception as e:
                print(e)

    # Get existing labels. Used to determine label.create() or label.edit()
    github_labels = [l.name for l in repo.get_labels()]

    # Label template JSON
    with open('labels.json') as f:
        labels = json.load(f)

    for label in labels:
        print(label)
    print('------------------\n')

    # Confirm list with user
    go = input("Label template loaded. Confirm load? [Y]: ")
    if go.lower() != 'y':
        print('Whoops! You entered --[{}]-- exiting...'.format(go))
    else:
        for l in labels:
            if l['name'] in github_labels:
                repo.get_label(l['name']).edit(l['name'], l['color'])
                print("{} exists, set COLOR={}".format(l['name'], l['color']))
            else:
                repo.create_label(l['name'], l['color'])
                print("Creating label, set NAME = {}, COLOR={}".format(l['name'], l['color']))
        print("Thank you for using my hack, have a nice day!")


if __name__ == '__main__':
    update_labels()
