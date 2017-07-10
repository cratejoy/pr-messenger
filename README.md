# pr-messenger

```sh
pip install git+https://github.com/cratejoy/pr-messenger.git

# Post a message (idempotent)
pr-messenger \
  --token 123123asldfasdf234r \
  --org cratejoy \
  --repo pr-messenger \
  --branch my-branch \
  --comment "Hello, world!"

# Update a status
pr-messenger \
  --token 123123asldfasdf234r \
  --org cratejoy \
  --repo pr-messenger \
  --sha 123asf3 \
  --status_name "ci/test" \
  --status-state "success" \
  --status_description "Your tests passed"
```
