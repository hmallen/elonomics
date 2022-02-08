from twitivity import Activity

account_activity = Activity()
account_activity.register_webhook("https://46c7-206-217-205-17.ngrok.io")
account_activity.subscribe()