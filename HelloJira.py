from jira import JIRA
import time

def main():
    jira_server = {
        'server': 'test URL test test'}

    jira_user = "testuser"
    jira_user = ""
    jira_password = ""
    t = time.perf_counter()
    jira = JIRA(options=jira_server, basic_auth=(jira_user, jira_password))
    print("Time connecting to jira: %.4f" % (time.perf_counter() - t))
    counter = 0

    t2 = time.perf_counter()

    notLast = True

    start_next_dataset = 0

    while notLast:
        jira_issues = jira.search_issues('project = DP AND key=DP-11', startAt=start_next_dataset, maxResults=100)

        if len(jira_issues) == 0:
            print("No more issues to work on")
            break
        for issue in jira_issues:
            transistions = jira.transitions(issue)
            # ,'comment': [{"add": {"body": "Transitioned by PyCharm"} }]
            jira.transition_issue(issue, '51')
            jira.add_comment(issue, "This is a comment by pyCharm")
            if issue.fields.customfield_10027 is not None and "pull" in issue.fields.customfield_10027:
                counter += 1
        print("*", end='', flush=True)

        start_next_dataset = start_next_dataset + 100

    print("Number of pull requests: %i" % counter)

if __name__ == '__main__':
    main()