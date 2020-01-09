
def current_beat():
    beat = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(beat):
            i = 0
        yield beat[i]
        i += 1


if __name__ == "__main__":
    beat_counter = current_beat()
    while True:
        print(next(beat_counter))
