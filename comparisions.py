import numpy as np

Term1 = [4, 6, 10, 12, 14, 16, 18, 20,
         22, 32, 47, 81, 120, 122, 157, 180]

Term2 = [47]

def intersect_count(postings1, postings2):
    result = []

    i = 0
    j = 0
    comparisons = 0

    while i < len(postings1) and j < len(postings2):

        comparisons += 1

        if postings1[i] == postings2[j]:
            result.append(postings1[i])
            i += 1
            j += 1

        elif postings1[i] < postings2[j]:
            i += 1

        else:
            j += 1

    return result, comparisons


result, comparisons = intersect_count(Term1, Term2)

print("Intersection:", result)
print("Comparisons:", comparisons)



skip_pointers = {
    0: 4,
    4: 8,
    8: 12
}


def intersect_with_skips(postings1, postings2, skip_length):
    result = []

    i = 0
    j = 0
    comparisons = 0

    # Create skip pointers
    skip_pointers = {}

    for pos in range(0, len(postings1) - skip_length, skip_length):
        skip_pointers[pos] = pos + skip_length

    while i < len(postings1) and j < len(postings2):

        comparisons += 1

        if postings1[i] == postings2[j]:
            result.append(postings1[i])
            i += 1
            j += 1

        elif postings1[i] < postings2[j]:

            if i in skip_pointers:
                skip_to = skip_pointers[i]

                comparisons += 1

                if postings1[skip_to] <= postings2[j]:
                    i = skip_to
                else:
                    i += 1
            else:
                i += 1

        else:
            j += 1

    return result, comparisons


skip_length = 4

result, comparisons = intersect_with_skips(
    Term1, Term2, skip_length
)

print("Intersection:", result)
print("Comparisons:", comparisons)



#OR Query

Term1 = [1, 2, 3, 5, 7]
Term2 = [2, 4, 6]

result = sorted(set(Term1).union(set(Term2)))

print("OR:", result)