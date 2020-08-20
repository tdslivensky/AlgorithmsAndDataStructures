# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):  
        # length of finish time    
        l = len(self.finish_time)
        # buffer
        s = self.size
        arrivaltime = request.arrived_at
        # time to process
        ttp = request.time_to_process
        # handels the first item
        if l <= s and l == 0:
            self.finish_time.append(arrivaltime + ttp)
            return Response(False,arrivaltime)

        # the finish time of the last packet in the queue
        prevFinish = self.finish_time[-1]

        # if the arrival time is greater than the finish time of the packet being worked on remove the first packet
        # and update the length
        if arrivaltime >= self.finish_time[0]:
            self.finish_time.pop(0)
        l = len(self.finish_time)
         
        # if there is not room in the quque 
        if l >= s:
            # and the arrival time is les than the previous finish time
            if arrivaltime < prevFinish:
                # reject packet
                r = Response(True,-1)
            elif arrivaltime == prevFinish:
                # accept the packet and add new finish time
                r = Response(False,prevFinish)
                self.finish_time.append(prevFinish + ttp)
            else:
                # else the whole queue has finished so clear and add to quque
                r = Response(False, arrivaltime)
                self.finish_time = []
                self.finish_time.append(arrivaltime + ttp)
        else:
            # there is room in the queue
            # the arrival time is after the last packet is complete
            if arrivaltime >= prevFinish:
                # acceot packet and add new finish time
                r = Response(False,arrivaltime)
                self.finish_time.append(arrivaltime + ttp)
            else:
                # accept the packet and append finish time 
                r = Response(False,prevFinish)
                self.finish_time.append(prevFinish + ttp)
        

        return r


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    # buffer_size = 3
    # n_requests = 6
    # requests = [Request(0, 2),Request(0, 3),Request(1, 4),Request(2, 2),Request(3, 2),Request(4, 1), Request(11, 1) ]

    # handel the null packet problem
    if n_requests != 0:
        buffer = Buffer(buffer_size)
        responses = process_requests(requests, buffer)

        for response in responses:
            print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
