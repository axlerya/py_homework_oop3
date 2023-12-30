from interfaces.Iterator import CustomIterator
from interfaces.Comporator import CustomComparator


class Flow:
    def __init__(self, study_groups: list):
        self.study_groups = study_groups

    def __iter__(self):
        return CustomIterator(self.study_groups)

    def __len__(self):
        count = 0
        for i in self.study_groups:
            count += 1
        return count

    def __gt__(self, other):
        return len(self.study_groups) > len(other.study_groups)

    def __ge__(self, other):
        return len(self.study_groups) >= len(other.study_groups)

    def __repr__(self):
        return f"{self.study_groups}"


class StreamComparator(CustomComparator):
    def __init__(self, list_flow_one: object, list_flow_two: object):
        super().__init__(list_flow_one, list_flow_two)

    def compare(self):
        return super().compare()


class ServiceFlow:
    def __init__(self, flow_list: list[list[object]]):
        self.flow_list = flow_list

    def sort_flows(self):
        for i in range(1, len(self.flow_list)):
            item = self.flow_list[i]
            i2 = i - 1
            while i2 >= 0 and self.flow_list[i2] > item:
                self.flow_list[i2 + 1] = self.flow_list[i2]
                i2 -= 1
            self.flow_list[i2 + 1] = item
        return self.flow_list


class Controller(ServiceFlow):
    def __init__(self, flow_list: list[list[object]]):
        super().__init__(flow_list)

    def sort_flows(self):
        return super().sort_flows()


groups_one = [1, 2, 3]
groups_two = [1, 2, 3, 2]
groups_three = [1, 2]
groups_four = [1, 2, 3]
groups_five = [1, 2, 3, 2, 1]

flow_one = Flow(groups_one)
flow_two = Flow(groups_two)
flow_three = Flow(groups_three)
flow_four = Flow(groups_four)
flow_five = Flow(groups_five)

a = StreamComparator(flow_one, flow_two)
print(a.compare())

flows_list = [flow_one, flow_two, flow_five, flow_four, flow_three]

b = Controller(flows_list)
print(b.sort_flows())
