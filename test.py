from github import Github

g = Github("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")

repo_name = 'solo11/ub-rl'

repo = g.get_repo(repo_name)
print(repo.name)

# List the contents of the repo
contents = repo.get_contents("")
for content_file in contents:
    print(content_file)

# Create a new file in the repo

# repo.create_file("test.py", "test", "test", branch="main")

# update a file
contents = repo.get_contents("test.py", ref="main")
with open('test.py') as f:
     contents_file = f.read()
repo.update_file(contents.path, "more tests 2", contents_file, contents.sha, branch="main")

# r = g.get_repo(repo)

# print(r.get_contents)

# for repo in g.get_user().get_repos():
#     print(repo.name)
#     repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    # print(dir(repo))

# create a repo
# read a file in a repo
# delete a file in a repo
# update a file  