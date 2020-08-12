import requests
import argparse

class GitSummaryInfo:

    def __init__(self, name="", clone_url="", latest_commit_date="", latest_commit_author=""):
        self.name = name
        self.clone_url = clone_url
        self.latest_commit_date = latest_commit_date,
        self.latest_commit_author = latest_commit_author

    def set_name(self, name):
        self.name = name

    def set_clone_url(self, clone_url):
        self.clone_url = clone_url

    def set_latest_commit_date(self, latest_commit_date):
        self.latest_commit_date = latest_commit_date

    def set_latest_commit_author(self, latest_commit_author):
        self.latest_commit_author = latest_commit_author


class GitSummaryCSVPrinter:

    def __init__(self, git_summaries):
        self.git_summaries = git_summaries

    def start(self):
        self.__print_header()
        for info in self.git_summaries:
            self.__print_info(info)

    def __print_header(self):
        print("{0},{1},{2},{3}".format("Name", "Clone URL", "Date of Latest Commit", "Author of Latest Commit"))

    def __print_info(self, info):
        print("{0},{1},{2},{3}".format(info.name, info.clone_url, info.latest_commit_date, info.latest_commit_author))


class GitSummarizer:

    def __init__(self, repositories):
        self.repositories = repositories
        self.headers = {'Accept': 'application/vnd.github.v3+json'}
        self.base_url = "https://api.github.com/repos/"

    def process(self):
        summaries = []

        for repo in self.repositories:
            git_summary = GitSummaryInfo()
            repo_info = self.__get_repo(repo)
            commits_info = self.__get_commits(repo)
            first_commit = commits_info[0]['commit']

            git_summary.set_name(repo_info['name'])
            git_summary.set_clone_url(repo_info['clone_url'])
            git_summary.set_latest_commit_date(first_commit['author']['date'])
            git_summary.set_latest_commit_author(first_commit['author']['name'])

            summaries.append(git_summary)

        self.__print(summaries)

    def __print(self, summaries):
        printer = GitSummaryCSVPrinter(summaries)
        printer.start()

    def __get_repo(self, repo):
        # TODO add exception handling
        repo_url = self.base_url + repo
        resp = self.__request(repo_url)
        return resp.json()

    def __get_commits(self, repo):
        # TODO add exception handling
        commits_url = self.base_url + repo + "/commits"
        resp = self.__request(commits_url)
        return resp.json()

    def __request(self, url):
        return requests.get(url, headers=self.headers)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get some git repo summaries.')
    parser.add_argument('repositories', type=str, nargs='+',
                        help='repositories with format $org/$name separated by space, e.g. facebook/react google/clusterfuzz')

    args = parser.parse_args()

    summary = GitSummarizer(args.repositories)
    summary.process()