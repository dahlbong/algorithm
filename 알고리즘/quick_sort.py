def quick_sort(arr, start, end):
    if start >= end:  # 리스트의 길이가 1 이하이면 종료
        return
    # 피벗을 리스트의 첫 번째 요소로 선택
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 왼쪽 포인터가 피벗보다 큰 값을 찾을 때까지 이동
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 오른쪽 포인터가 피벗보다 작은 값을 찾을 때까지 이동
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        # 교차되지 않은 경우, L과 R이 가리키는 요소를 스왑
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            print(f"스왑: {arr}")
        else:
            # 교차되었으면 피벗과 R이 가리키는 요소를 스왑
            arr[pivot], arr[right] = arr[right], arr[pivot]
            print(f"피벗 스왑: {arr}")
    # 피벗이 고정된 위치에서 나누어 재귀적으로 퀵 정렬을 수행
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)
# 예제 사용
unsorted_list = list(map(int, input().split()))
quick_sort(unsorted_list, 0, len(unsorted_list) - 1)
print(f"정렬된 리스트: {unsorted_list}")