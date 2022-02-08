from twitivity import Event
import json


class StreamEvent(Event):
    CALLBACK_URL: str = "https://46c7-206-217-205-17.ngrok.io"

    def on_data(self, data: json) -> None:
        # process data
        print(data)


if __name__ == '__main__':
    stream_events = StreamEvent()
    stream_events.listen()