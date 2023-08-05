

class Rank():
    def __init__(self):
        self.pros = None

    def rank(self, pros):
        self.pros = pros
        return self.pros
    
class BaseRank(Rank):
    def __init__(self):
        pass

    def rank(self, pros):
        self.pros = pros
        return [1,2,3,4,5,6,7,8]
    
class NewRank(Rank):
    def __init__(self):
        pass

    def rank(self, pros):
        self.pros = pros
        return [1,4,5,6,2,3]
    
class QualityRank(Rank):
    def __init__(self):
        pass

    def rank(self, pros):
        self.pros = pros
        return [1,2,3,5,6,8,4,7]
    
class SlidingWindowRank(Rank):
    def __init__(self, window, rank_map):
        self.window = window
        self.rank_map = rank_map

    def rank(self, pros):
        self.pros = pros
        window_len = 0
        ranked_pros_list = []
        rank_ctr_map = {}
        for k in self.rank_map:
            rank_ctr_map[k] = 0
    
        while len(ranked_pros_list) < len(self.pros):
            if window_len == len(self.window):
                window_len = 0
            
            rank_name = self.window[window_len]
            pro = self.rank_map[rank_name].rank(pros)[rank_ctr_map[rank_name]]
            if pro in ranked_pros_list:
                while pro in ranked_pros_list and rank_ctr_map[rank_name]+1 < len(self.rank_map[rank_name].rank(pros)):
                    pro = self.rank_map[rank_name].rank(pros)[rank_ctr_map[rank_name]]
                    if rank_ctr_map[rank_name]+1 < len(self.rank_map[rank_name].rank(pros)):
                        rank_ctr_map[rank_name] += 1
                if pro not in ranked_pros_list:
                    ranked_pros_list.append(pro)
            else:
                rank_ctr_map[rank_name] += 1
                ranked_pros_list.append(pro)

            
            window_len += 1
           
        return ranked_pros_list
    
def main():
    pros_list = [1,2,3,4,5,6,7,8]
    base_rank = BaseRank()
    new_rank = NewRank()
    quality_rank = QualityRank()

    window = ["Base", "New", "Base", "Quality", "New", "Base"]
    rank_map = {
        "Base": base_rank,
        "New": new_rank,
        "Quality": quality_rank,
    }

    sliding_window_rank = SlidingWindowRank(window, rank_map)
    print(sliding_window_rank.rank(pros_list))

if __name__ == "__main__":
    main()