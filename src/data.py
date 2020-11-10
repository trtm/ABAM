#!/usr/bin/env python

import pandas as pd

#################################################################################
# SENTENCES

ABAM_DATA_SENTENCES_without_sentences = pd.read_csv(
        './data/ABAM_DATA_SENTENCES.tsv', 
        sep='\t')
print(len(ABAM_DATA_SENTENCES_without_sentences))

ABAM_SENTENCES = pd.read_csv(
        './data/ABAM_SENTENCES.tsv', 
        sep='\t')
print(len(ABAM_SENTENCES))

assert len(ABAM_DATA_SENTENCES_without_sentences)==len(ABAM_SENTENCES)

ABAM_DATA_SENTENCES = pd.merge(
        ABAM_DATA_SENTENCES_without_sentences[['topic', 'sentence_hash', 'stance', 'aspect', 'inner', 'cross']], 
        ABAM_SENTENCES, 
        on='sentence_hash')
ABAM_DATA_SENTENCES = ABAM_DATA_SENTENCES[['topic', 'sentence_hash', 'sentence', 'stance', 'aspect', 'inner', 'cross']]
print(len(ABAM_DATA_SENTENCES))

print(ABAM_DATA_SENTENCES[['topic', 'sentence_hash']].groupby('topic').count())

#################################################################################
# SEGMENTS

ABAM_DATA_SEGMENTS_without_segments = pd.read_csv(
        './data/ABAM_DATA_SEGMENTS.tsv', 
        sep='\t')
print(len(ABAM_DATA_SEGMENTS_without_segments))

ABAM_SEGMENTS = pd.read_csv(
        './data/ABAM_SEGMENTS.tsv', 
        sep='\t')
print(len(ABAM_SEGMENTS))

assert len(ABAM_DATA_SEGMENTS_without_segments)==len(ABAM_SEGMENTS)

ABAM_DATA_SEGMENTS = pd.merge(
        ABAM_DATA_SEGMENTS_without_segments[['topic', 'sentence_hash', 'segment_count', 'segment_hash', 'stance', 'aspect', 'inner', 'cross']], 
        ABAM_SEGMENTS, on='segment_hash')
ABAM_DATA_SEGMENTS = ABAM_DATA_SEGMENTS[['topic', 'sentence_hash', 'segment_count', 'segment_hash', 'segment', 'stance', 'aspect', 'inner', 'cross']]
print(len(ABAM_DATA_SEGMENTS))

print(ABAM_DATA_SEGMENTS[['topic', 'segment_hash']].groupby('topic').count())
