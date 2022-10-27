''' exercise scale '''

class Scale:
    sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    flat = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
    in_sharp_scale = ['a', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'e', 'b', 'f#', 'c#', 'g#', 'd#']
    in_flat_scale = [ 'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb', 'eb']
    intervals = {'m': 1, 'M': 2, 'A': 3}
    
    def __init__(self, tonic):
        self.tonic = tonic.capitalize()
        self.chromatic_scale = Scale.sharp[Scale.sharp.index(self.tonic)::] + Scale.sharp[:Scale.sharp.index(self.tonic)] if tonic in Scale.in_sharp_scale \
            else Scale.flat[Scale.flat.index(self.tonic)::] + Scale.flat[:Scale.flat.index(self.tonic)]
        

    def chromatic(self):
        return self.chromatic_scale

    def interval(self, intervals):
        lst_to_ret, index = [self.tonic], 0
        for char in intervals:
            index += Scale.intervals[char]
            if index >= len(self.chromatic_scale):
                index -= len(self.chromatic_scale)
            lst_to_ret.append(self.chromatic_scale[index])
        return lst_to_ret

if __name__ == '__main__':
    skala = Scale('a')
    print(skala.chromatic())