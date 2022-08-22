class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs[0]:
            return ""

        result = ""
        strs_min_len = min([len(_str) for _str in strs])
        for idx in range(strs_min_len):

            common_prefix = ""
            for _str in strs:
                if common_prefix == "":
                    common_prefix = _str[: idx + 1]
                    continue
                if common_prefix != _str[: idx + 1]:
                    return result
            result = common_prefix

        return result
