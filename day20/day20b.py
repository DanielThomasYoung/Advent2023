from dataclasses import dataclass
from math import lcm


@dataclass
class FlipFlop:
    outputs: list[str]
    state: bool


@dataclass
class Conjunction:
    inputs: dict
    outputs: list[str]


@dataclass
class Pulse:
    source: str
    target: str
    state: bool


def main():
    with open("day20.txt", "r") as file:
        lines = file.readlines()

    nodes = {}

    for line in lines:
        formatted_line = line.strip().replace(",", "").split()

        if formatted_line[0][0] == "b":
            broadcaster = formatted_line[2:]

        elif formatted_line[0][0] == "&":
            nodes[formatted_line[0][1:]] = Conjunction({}, formatted_line[2:])

    for node in nodes:
        for target in nodes[node].outputs:
            if target in nodes:
                nodes[target].inputs[node] = False

    for line in lines:
        formatted_line = line.strip().replace(",", "").split()

        if formatted_line[0][0] == "%":
            name = formatted_line[0][1:]
            outputs = formatted_line[2:]
            flip_flop = FlipFlop(state=False, outputs=outputs)
            nodes[name] = flip_flop

            for target in outputs:
                if (
                    target in nodes
                    and nodes[target].__class__.__name__ == "Conjunction"
                ):
                    nodes[target].inputs[name] = False

    cycles = []

    for press_count in range(1, 50000):
        pulses = [
            Pulse(source="initial", target=target, state=False)
            for target in broadcaster
        ]

        while pulses:
            new_pulses = []
            for pulse in pulses:
                if pulse.target == "ll" and pulse.state:
                    new_cycle = True
                    for cycle in cycles:
                        new_cycle = new_cycle and press_count % cycle
                    if new_cycle:
                        cycles.append(press_count)
                    print(press_count)

                if pulse.target not in nodes:
                    continue

                if nodes[pulse.target].__class__.__name__ == "Conjunction":
                    nodes[pulse.target].inputs[pulse.source] = pulse.state

                    high = True
                    for con_input in nodes[pulse.target].inputs.values():
                        high = high and con_input

                    for next_target in nodes[pulse.target].outputs:
                        new_pulses.append(
                            Pulse(
                                source=pulse.target, target=next_target, state=not high
                            )
                        )

                elif not pulse.state:
                    nodes[pulse.target].state = not nodes[pulse.target].state

                    for next_target in nodes[pulse.target].outputs:
                        new_pulses.append(
                            Pulse(
                                source=pulse.target,
                                target=next_target,
                                state=nodes[pulse.target].state,
                            )
                        )

            pulses = new_pulses

    return lcm(*cycles)


if __name__ == "__main__":
    print(main())
