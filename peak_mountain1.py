while j<len(arr)-1 and arr[j]>arr[j+1]:
            cnt += 1
            j += 1
        ans = max(cnt,ans)
        i=j
    else:
        i += 1
print(ans)