#!/usr/bin/env python

"""
This script computes the following binary metrics
  * tp
  * fp
  * fn
  * precision
  * recall

Tests can be executed by running
> python binary_metrics.py
"""


def __get_existing_taxa(rank):
  """ Return set of taxids with abundance > 0

  >>> __get_existing_taxa(query_rank)
  [123]

  :param rank: Set of taxids of specific rank
  :return: list of taxids
  """
  return list(k for k, v in rank.iteritems() if v > 0)


def __get_non_existing_taxa(rank):
  """Return set of taxids with abundance < 0
  >>> __get_non_existing_taxa(query_rank)
  [1232]

  :param rank: Set of taxids of specific rank
  :return: list of taxids
  """

  return list(k for k, v in rank.iteritems() if v <= 0)


def __get_tp(rank_query, rank_truth):
  """ Returns true positive
  >>> __get_tp(test_query_rank, test_truth_rank)
  1

  """
  rank_query = __get_existing_taxa(rank_query)
  rank_truth = __get_existing_taxa(rank_truth)
  return len(list(set(rank_query).intersection(rank_truth)))


def __get_fp(rank_query, rank_truth):
  """ Returns false positive
  >>> __get_fp(test_query_rank, test_truth_rank)
  0

  """

  rank_query = __get_non_existing_taxa(rank_query)
  rank_truth = __get_existing_taxa(rank_truth)
  return len(list(set(rank_query).intersection(rank_truth)))


def __get_fn(rank_query, rank_truth):
    """ Returns false negative
    >>> __get_fn(test_query_rank, test_truth_rank)
    0

    """
    rank_query = __get_existing_taxa(rank_query)
    rank_truth = __get_non_existing_taxa(rank_truth)
    return len(list(set(rank_query).intersection(rank_truth)))


def precision(tp, fp):
    return tp/(tp+fp)


def recall(tp, fn):
    return tp/(tp+fn)


def compute_rank_metrics(rank_query, rank_truth):
    """ Returns metrics for one rank
    >>> compute_rank_metrics(test_query_rank, test_truth_rank)
    (1, 1, 1, 0, 0)

    """
    tp = __get_tp(rank_query, rank_truth)
    fn = __get_fn(rank_query, rank_truth)
    fp = __get_fp(rank_query, rank_truth)
    return precision(tp, fp), recall(tp, fn), tp, fn, fp


def compute_tree_metrics(query, truth):
    """ Return metrics for tree
    >>> compute_tree_metrics(query_tree, truth_tree)
    {'species': (1, 1, 1, 0, 0)}
    """
    return {rank: compute_rank_metrics(taxids, truth[rank]) for rank, taxids in query.items()}

if __name__ == "__main__":
    import doctest
    test_query_rank = dict()
    test_query_rank[123] = 0.1
    test_query_rank[1232] = 0.0

    test_truth_rank = dict()
    test_truth_rank[123] = 0.1
    test_truth_rank[1232] = 0.0

    test_truth_tree = dict()
    test_truth_tree["species"] = test_truth_rank

    test_query_tree = dict()
    test_query_tree["species"] = test_query_rank

    doctest.testmod(extraglobs={'query_rank': test_query_rank,
                                'truth_rank': test_truth_rank,
                                'truth_tree': test_truth_tree,
                                'query_tree': test_query_tree})