def dist_sift_up(values, elements, element_index, distances):
    parent_index = (element_index - 1) // 2
    while element_index != 0 and distances[values[element_index]] < distances[values[parent_index]]:
        elements[values[element_index]], elements[values[parent_index]] = parent_index, element_index
        values[element_index], values[parent_index] = values[parent_index], values[element_index]
        element_index = parent_index
        parent_index = (element_index - 1) // 2


def extract_min(values, elements, distances):
    if not len(values):
        return None
    tmp = values[0]
    values[0] = values[-1]
    values.pop()
    if len(values):
        elements[values[0]] = 0
    dist_sift_down(values, elements, 0, distances)
    return tmp


def dist_sift_down(values, elements, element_index, distances):
    youngest_child = 2 * element_index + 1
    oldest_child = 2 * element_index + 2
    while youngest_child < len(values):
        current_element = element_index
        if distances[values[youngest_child]] < distances[values[element_index]]:
            current_element = youngest_child
        if oldest_child < len(values) and distances[values[oldest_child]] < distances[values[current_element]]:
            current_element = oldest_child
        if element_index == current_element:
            break
        elements[values[element_index]], elements[values[current_element]] = current_element, element_index
        values[element_index], values[current_element] = values[current_element], values[element_index]
        element_index = current_element
        youngest_child = 2 * element_index + 1
        oldest_child = 2 * element_index + 2


if __name__ == '__main__':
    input_data = list(map(int, input().split()))
    n, m = input_data[0], input_data[1]  # n - num of vertexes, m - num of edges, s - start vertex, f - final vertex
    regions = input_data[2:]
    gr = [[] for _ in range(n + 1)]
    for i in range(m):
        ed = tuple(map(int, input().split()))  # edge
        gr[ed[0]].append([ed[1], ed[2]])
        gr[ed[1]].append([ed[0], ed[2]])
        if i < len(regions):
            gr[-1].append([regions[i], 1])
    d = [float('inf')] * (n + 1)  # distances
    d[-1] = -1
    h, el = [n] + [i for i in range(n)], [i + 1 for i in range(n)] + [0]  # heap
    r = [-1] * (n + 1)  # regions of cities
    while h:
        current_el = extract_min(h, el, d)
        if d[current_el] == float('inf'):
            break
        for vertex, weight in gr[current_el]:
            if d[vertex] > d[current_el] + weight:
                d[vertex] = d[current_el] + weight
                dist_sift_up(h, el, el[vertex], d)
                if r[current_el] == -1:
                    r[vertex] = vertex
                else:
                    r[vertex] = r[current_el]
    r.pop()
    print(*r, sep='\n')
