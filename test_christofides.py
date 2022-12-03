import unittest

from christofides import *
from graph import *


class MyTestCase(unittest.TestCase):

    def test_odd_deg_vertices1(self):
        # Given
        G1 = graph({'0': {'1': 10, '2': 8}, '1': {'0': 10, '2': 2, '3': 5, '4': 6},
                    '2': {'0': 8, '1': 2}, '3': {'1': 5, '4': 1},
                    '4': {'1': 6, '3': 1}})
        expected_result = []

        # When
        result = odd_deg_vertices(G1)

        # Then
        self.assertEqual(expected_result, result)

    def test_odd_deg_vertices2(self):
        # Given
        G2 = graph({'0': {'2': 2, '3': 2}, '1': {'2': 2, '3': 5},
                    '2': {'0': 2, '1': 2, '3': 2}, '3': {'0': 2, '1': 5, '2': 2}})
        expected_result = ['2', '3']

        # When
        result = odd_deg_vertices(G2)

        # Then
        self.assertEqual(expected_result, result)

    def test_odd_deg_vertices3(self):
        # Given
        G3 = graph({'0': {'1': 0.1, '2': 2.5, '3': 2.8}, '1': {'0': 8, '2': 2, '3': 15},
                    '2': {'0': 27.5, '1': 102, '3': 4.2}, '3': {'0': 32, '1': 5, '2': 0.2}})
        expected_result = ['0', '1', '2', '3']

        # When
        result = odd_deg_vertices(G3)

        # Then
        self.assertEqual(expected_result, result)

    # def test_multigraph1(self):
    #     # Given
    #     H1 = graph({'0': {'1': 1, '3': 2, '4': 4}, '1': {'0': 1, '2': 2},
    #                 '2': {'1': 2}, '3': {'0': 2, '4': 1},
    #                 '4': {'0': 4, '3': 1}})
    #     K1 = graph({'0': {'1': 1, '3': 2}, '1': {'0': 1, '4': 6},
    #                 '2': {}, '3': {'0': 2, '4': 1},
    #                 '4': {'1': 6, '3': 1}})
    #
    #     expected_result = nx.MultiGraph(graph({'0': {'1': 1, '1': 1, '3': 2, '3': 2, '4': 4},
    #                                            '1': {'0': 1, '0': 1, '2': 2, '4': 6},
    #                                  '2': {'1': 2}, '3': {'0': 2, '0': 2, '4': 1, '4': 1},
    #                                  '4': {'0': 4, '1': 6, '3': 1, '3': 1}}).to_nx())
    #
    #     # When
    #     result = multigraph(H1.to_nx(), K1.to_nx())
    #
    #     # Then
    #     self.assertEqual(expected_result, result)

    # def test_multigraph2(self):
    #     # Given
    #     H2 = graph({'0': {'1': 1, '2': 2}, '1': {'0': 1}, '2': {'0': 2}})
    #     K2 = graph({'1': {'2': 2}, '2': {'1': 2}})
    #
    #     expected_result = graph({'0': {'1': 1, '2': 2}, '1': {'0': 1, '2': 2}, '2': {'0': 2, '1': 2}}).to_nx()
    #
    #     # When
    #     result = multigraph(H2, K2)
    #
    #     # Then
    #     self.assertEqual(expected_result, result)
    #
    # def test_multigraph3(self):
    #     # Given
    #     H3 = graph({'0': {'1': 1.5, '2': 0.2, '3': 23, '4': 4.5}, '1': {'0': 1.5, '2': 2.3, '3': 7.5, '4': 6},
    #                 '2': {'0': 0.2, '1': 2.3, '3': 2, '4': 22}, '3': {'0': 23, '1': 7.5, '2': 2, '4': 9.1},
    #                 '4': {'0': 4.5, '1': 6, '2': 22, '3': 9.1}})
    #     K3 = graph({'0': {'1': 1.5}, '1': {'0': 1.5}})
    #     expected_result = graph({'0': {'1': 1.5, '1': 1.5, '2': 0.2, '3': 23, '4': 4.5},
    #                              '1': {'0': 1.5, '0': 1.5, '2': 2.3, '3': 7.5, '4': 6},
    #                              '2': {'0': 0.2, '1': 2.3, '3': 2, '4': 22}, '3': {'0': 23, '1': 7.5, '2': 2, '4': 9.1},
    #                              '4': {'0': 4.5, '1': 6, '2': 22, '3': 9.1}}).to_nx()
    #
    #     # When
    #     result = multigraph(H3, K3)
    #
    #     # Then
    #     self.assertEqual(expected_result, result)
    #
    def test_ham_from_eul1(self):
        # Given
        E1 = nx.eulerian_circuit(graph({'0': {'1': 1, '4': 4}, '1': {'0': 1, '2': 2, '3': 5, '4': 6},
                                        '2': {'1': 2, '3': 2}, '3': {'1': 5, '2': 2},
                                        '4': {'0': 4, '1': 6}}).to_nx())

        expected_result1 = ['1', '0', '4', '3', '2']
        expected_result2 = ['2', '1', '0', '4', '3']
        expected_result3 = ['3', '2', '1', '0', '4']
        expected_result4 = ['4', '3', '2', '1', '0']
        expected_result5 = ['0', '4', '3', '2', '1']
        expected_result6 = ['1', '2', '3', '4', '0']
        expected_result7 = ['0', '1', '2', '3', '4']
        expected_result8 = ['4', '0', '1', '2', '3']
        expected_result9 = ['3', '4', '0', '1', '2']
        expected_result10 = ['2', '3', '4', '0', '1']
        expected_result11 = ['1', '0', '4', '2', '3']
        expected_result12 = ['3', '1', '0', '4', '2']
        expected_result13 = ['2', '3', '1', '0', '4']
        expected_result14 = ['4', '2', '3', '1', '0']
        expected_result15 = ['0', '4', '2', '3', '1']
        expected_result16 = ['1', '2', '3', '0', '4']
        expected_result17 = ['4', '1', '2', '3', '0']
        expected_result18 = ['0', '4', '1', '2', '3']
        expected_result19 = ['3', '0', '4', '1', '2']
        expected_result20 = ['2', '3', '0', '4', '1']
        expected_result21 = ['1', '3', '2', '0', '4']
        expected_result22 = ['4', '1', '3', '2', '0']
        expected_result23 = ['0', '4', '1', '3', '2']
        expected_result24 = ['2', '0', '4', '1', '3']
        expected_result25 = ['3', '2', '0', '4', '1']
        expected_result26 = ['1', '3', '2', '4', '0']
        expected_result27 = ['0', '1', '3', '2', '4']
        expected_result28 = ['4', '0', '1', '3', '2']
        expected_result29 = ['2', '4', '0', '1', '3']
        expected_result30 = ['3', '2', '4', '0', '1']

        # When
        result = ham_from_eul(E1)

        # Then
        self.assertTrue(result in [expected_result1, expected_result2, expected_result3, expected_result4,
                                   expected_result5, expected_result6, expected_result7, expected_result8,
                                   expected_result9, expected_result10, expected_result11, expected_result12,
                                   expected_result13, expected_result14, expected_result15, expected_result16,
                                   expected_result17, expected_result18, expected_result19, expected_result20,
                                   expected_result21, expected_result22, expected_result23, expected_result24,
                                   expected_result25, expected_result26, expected_result27, expected_result28,
                                   expected_result29, expected_result30])

    def test_ham_from_eul2(self):
        # Given
        E2 = nx.eulerian_circuit(graph({'0': {'2': 2, '3': 2}, '1': {'2': 2, '3': 5},
                                        '2': {'0': 2, '1': 2}, '3': {'0': 2, '1': 5}}).to_nx())
        expected_result1 = ['0', '2', '1', '3']
        expected_result2 = ['3', '0', '2', '1']
        expected_result3 = ['1', '3', '0', '2']
        expected_result4 = ['2', '1', '3', '0']
        expected_result5 = ['0', '3', '1', '2']
        expected_result6 = ['2', '0', '3', '1']
        expected_result7 = ['1', '2', '0', '3']
        expected_result8 = ['3', '1', '2', '0']

        # When
        result = ham_from_eul(E2)

        # Then
        self.assertTrue(result in [expected_result1, expected_result2, expected_result3, expected_result4,
                                   expected_result5, expected_result6, expected_result7, expected_result8])

    def test_ham_from_eul3(self):
        # Given
        E3 = nx.eulerian_circuit(graph({'0': {'1': 1, '2': 2}, '1': {'0': 1, '2': 2}, '2': {'0': 2, '1': 2}}).to_nx())

        expected_result1 = ['0', '1', '2']
        expected_result2 = ['0', '2', '1']
        expected_result3 = ['1', '2', '0']
        expected_result4 = ['2', '1', '0']
        expected_result5 = ['2', '0', '1']
        expected_result6 = ['1', '0', '2']

        # When
        result = ham_from_eul(E3)

        # Then
        self.assertTrue(result in [expected_result1, expected_result2, expected_result3,
                                   expected_result4, expected_result5, expected_result6])

    # def test_christofides_1(self):
    #     # Given
    #     D1 = graph({'0': {'1': 1, '2': 2, '3': 2, '4': 4}, '1': {'0': 1, '2': 2, '3': 5, '4': 6},
    #                 '2': {'0': 2, '1': 2, '3': 2, '4': 2}, '3': {'0': 2, '1': 5, '2': 2, '4': 1},
    #                 '4': {'0': 4, '1': 6, '2': 2, '3': 1}})
    #     expected_result = ['0', '3', '4', '2', '1']
    #
    #     # When
    #     result = christofides(D1)
    #
    #     # Then
    #     self.assertEqual(expected_result, result)
    #
    # def test_christofides_2(self):
    #     # Given
    #     D2 = graph({'0': {'1': 10, '2': 2, '3': 2, '4': 24, '5': 15}, '1': {'0': 10, '2': 12, '3': 50, '4': 26, '5': 7},
    #                 '2': {'0': 2, '1': 12, '3': 29, '4': 8, '5': 31}, '3': {'0': 2, '1': 50, '2': 29, '4': 1, '5': 14},
    #                 '4': {'0': 24, '1': 26, '2': 8, '3': 1, '5': 10},
    #                 '5': {'0': 15, '1': 7, '2': 31, '3': 14, '4': 10}})
    #     expected_result = ['0', '3', '4', '2', '1', '5']
    #
    #     # When
    #     result = christofides(D2)
    #
    #     # Then
    #     self.assertEqual(expected_result, result)
    #
    # def test_christofides_3(self):
    #     # Given
    #     D3 = graph({'0': {}})
    #     expected_result = ['0', '3', '4', '2', '1', '5']
    #
    #     # When
    #     result = christofides(D3)
    #
    #     # Then
    #     self.assertEqual(expected_result, result)


if __name__ == '__christofides__':
    unittest.christofides()
