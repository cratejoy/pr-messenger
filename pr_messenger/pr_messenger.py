import argparse
import github


def add_comment_to_pr(pr, comment_body):
    for comment in pr.get_issue_comments():
        if comment.body == comment_body:
            print("Comment already exists")
            return

    pr.create_issue_comment(comment_body)
    print("Comment created")


def find_pr_and_add_comment(client, org, repo, branch, comment, **kwargs):
    grepo = client.get_repo('{}/{}'.format(org, repo))
    for pr in grepo.get_pulls(sort='updated')[0:100]:
        if pr.head.ref == branch:
            add_comment_to_pr(pr, comment)
            return

    print("No PR found for branch")


def add_sha_status(client, org, repo, sha, status_name, status_state, status_url, status_description, **kwargs):
    grepo = client.get_repo('{}/{}'.format(org, repo))
    commit = grepo.get_commit(sha)

    status = commit.create_status(
        status_state,
        context=status_name,
        target_url=status_url or github.GithubObject.NotSet,
        description=status_description or github.GithubObject.NotSet
    )

    print("Status created: {}".format(status.url))


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--token', required=True)
    parser.add_argument('--org', required=True)
    parser.add_argument('--repo', required=True)

    # For PR comments
    parser.add_argument('--branch', required=False)
    parser.add_argument('--comment', required=False)

    # For status updates
    parser.add_argument('--sha', required=False)
    parser.add_argument('--status_name', required=False)
    parser.add_argument('--status_state', required=False)
    parser.add_argument('--status_url', required=False)
    parser.add_argument('--status_description', required=False)

    cli_args = parser.parse_args()

    client = github.Github(login_or_token=cli_args.token)

    if cli_args.status_name and cli_args.sha:
        add_sha_status(client, **cli_args.__dict__)
    if cli_args.comment and cli_args.branch:
        find_pr_and_add_comment(client, **cli_args.__dict__)


if __name__ == '__main__':
    main()
