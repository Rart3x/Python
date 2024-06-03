class calculator:
    '''Calculator class'''

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''Dot product calculator method'''

        total = 0

        for i in range(len(V1)):
            total += V1[i] + V2[i]
        print("Dot product is:", total)

    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''Add Vec calculator method'''

        vec = [0] * max(len(V1), len(V2))

        for i in range(len(V1)):
            vec[i] += V1[i] + V2[i]
        print("Add Vector is:", vec)

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''Sous Vec calculator method'''

        vec = [0] * max(len(V1), len(V2))

        for i in range(len(V1)):
            vec[i] += V1[i] - V2[i]
        print("Sous Vector is:", vec)
