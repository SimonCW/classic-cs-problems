def main() -> None:
    orig_gene: str = "ATTG"
    compressed = CompressedGene(orig_gene)
    print(bin(compressed.bit_string))
    print(compressed)


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
        for nucleo in gene.upper():
            self.bit_string <<= 2
            if nucleo == "A":
                self.bit_string |= 0b00
            elif nucleo == "T":
                self.bit_string |= 0b11
            elif nucleo == "G":
                self.bit_string |= 0b10
            else:
                raise ValueError(f"invalid Nucleo {nucleo}")

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += "A"
            elif bits == 0b11:
                gene += "T"
            elif bits == 0b10:
                gene += "G"
            else:
                raise ValueError(f"invalid bits {bits}")
        return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()


if __name__ == "__main__":
    main()
