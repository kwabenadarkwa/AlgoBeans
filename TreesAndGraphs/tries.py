from string import ascii_lowercase as alc
from typing import List, Optional, Self


class TrieNode:
    def __init__(self, character):
        self.character = character
        self.children: List[Optional[Self]] = [None] * 26
        self.is_last_node: bool = False


class Trie:
    def __init__(self):
        self.root: List[TrieNode] = []
        for c in alc:
            self.root.append(TrieNode(c))

    @classmethod
    def find_index_based_on_character(cls, c) -> int:
        return ord(c) - ord("a")

    def add_word(self, word):
        trie_node = self.root
        for i in range(len(word)):
            index = Trie.find_index_based_on_character(word[i])

            if trie_node[index] is None:
                trie_node[index] = TrieNode(word[i])

            if i == len(word) - 1:
                trie_node[index].is_last_node = True  # type:ignore

            trie_node = trie_node[index].children  # type:ignore

    def find_word(self, word):
        trie_node = self.root
        for i in range(len(word)):
            index = Trie.find_index_based_on_character(word[i])

            if trie_node[index] is None:
                return False

            trie_node = trie_node[index].children  # type:ignore

        return True

    def find_prefix(self, prefix):
        pass

    def print_trie(self, node=None, prefix="", is_root=True):
        if is_root:
            node = self.root
            print("Trie Structure:")
            for i, child in enumerate(node):
                if isinstance(child, TrieNode) and child != None:
                    char = chr(i + ord("a"))
                    end_marker = " *" if child.is_last_node else ""
                    print(f"{char}{end_marker}")
                    self._print_trie_helper(child.children, f"  ", char)

    def _print_trie_helper(self, node, indent, parent_char):
        for i, child in enumerate(node):
            if isinstance(child, TrieNode) and child != None:
                char = chr(i + ord("a"))
                end_marker = " *" if child.is_last_node else ""
                print(f"{indent}{char}{end_marker}")
                self._print_trie_helper(child.children, indent + "  ", char)


if __name__ == "__main__":
    trie = Trie()
    trie.add_word("thing")
    trie.add_word("tree")
    trie.add_word("trip")
    trie.add_word("kwabena")
    print(trie.find_word("trip"))
    # trie.print_trie()
