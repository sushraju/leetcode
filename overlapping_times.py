#!/usr/bin/env python

def find_max_overlap_times(video_calls_times):
    max_concurrent_videos = 1
    for i in range(len(video_calls_times)):
        s_i, e_i = video_calls_times[i]
        n_max_concurrent_videos = 1
        for j in range((i+1), len(video_calls_times)):
            s_j, e_j = video_calls_times[j]
            if s_j < e_i:
                n_max_concurrent_videos += 1
            else:
                break
        if max_concurrent_videos == 1 or max_concurrent_videos < n_max_concurrent_videos:
            max_concurrent_videos = n_max_concurrent_videos
    
    return max_concurrent_videos

def main():
    video_calls_times = [(1,4), (2,5), (3,8), (4,9)]
    print(find_max_overlap_times(video_calls_times))

if __name__ == "__main__":
    main()