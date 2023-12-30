class CustomComparator:
    def __init__(self, list_flow_one: object, list_flow_two: object):
        self.list_flow_one = list_flow_one
        self.list_flow_two = list_flow_two
        
    def compare(self):
        if len(self.list_flow_one) == len(self.list_flow_two):
            return 0
        elif len(self.list_flow_one) > len(self.list_flow_two):
            return 1
        else:
            return -1