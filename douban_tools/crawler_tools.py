

def find_sid(raw_str: str) -> str:
    '''
        Args:
            raw_str: a html info string contains sid
        Returns:
            sid
    '''
    assert type(raw_str) == str, \
        '''the type of raw_str must be str'''
    start_index = raw_str.find('sid:')
    return raw_str[start_index: start_index + 13]


if __name__ == "__main__":
    raw_str = "haha sid: 20427187， "
    print(find_sid(raw_str))
