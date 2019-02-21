# =============================================================================
# Problem Set 2
# Name: Hin Mo
# Collaborators: Laplace
# Time:45mins
# =============================================================================

def constrainedMatchPair(firstMatch,secondMatch,length):
    '''
    this function is able to find near matches like a*gc or at*c, 
    but *tgc or atg* is temporarily not.
    '''
    n_tuple=()
    m=length
    for n in firstMatch:
        for k in secondMatch:
            if n<k:
                if n+m+1==k:
                    n_tuple+=(n,)
    return n_tuple