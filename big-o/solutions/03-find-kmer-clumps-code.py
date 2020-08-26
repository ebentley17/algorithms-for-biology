def clumping_kmers(genome, kmer_length, window_length, min_kmer_count):
    '''
    This function finds clusters of k-mers in a genome.

    * Accepts as input:
        * `genome` — a string representing the genome of an organism.
        * `kmer_length` - an integer representing the length of the k-mers to be considered for clumping.
        * `window_size` — an integer representing the size of the "region of interest".
        * `min_kmer_count` – an integer representing the minimum number of duplicate k-mers found within `window_size` of each other to be considered a cluster.
    
    * Returns as output:
        * A dictionary mapping all the k-mers that satisfy the clustering criteria to a list of all the start locations within `genome` for those clusters.
        * Each position in the list should be a start location of the k-mer satisfying the clustering criteria.
            * For example, consider the genome `'ATATGATGATAT'` the 3-mer `'ATG'` a `window_length` of 10, and a `min_kmer_count`of 2.
            * In reality, we could map this window to all the positions `[0, 1, 2]` — but all of these positions contain the SAME cluster, and the most relevant of those positions is `2` because it is the start of the first copy of our k-mer `'ATG'`. 
                * Including positions 0 and 1 in our solution would be both redundant and less useful in subsequent analysis. 
    '''
    # Collect all the unique kmers and where they occur
    kmers = {}
    for start_position in range(len(genome) - kmer_length + 1):
        kmer = genome[start_position:start_position+kmer_length]
        if kmer not in kmers:
            kmers[kmer] = []
        
        kmers[kmer].append(start_position)

    # For each kmer and it's locations determine if they meet
    # the min-count within the window length.
    candidate_kmers = {}
    for kmer, locations in kmers.items():
        if len(locations) < min_kmer_count:
            continue

        cluster_window_start_points = []
        
        start_pos = 0
        start_val = locations[start_pos]
        for end_pos in range(0, len(locations)):
            end_val = locations[end_pos]

            # advance the start position until it's
            # within window_length of the end pos
            while (end_val + kmer_length) - start_val >= window_length:
                start_pos += 1
                start_val = locations[start_pos]

            # if there are at least min_kmer_count in this window
            # it's a candidate
            if (end_pos - start_pos) + 1 > min_kmer_count:
                cluster_window_start_points.append(start_val) 

        # If we found at least one window for this kmer, add them.
        if len(cluster_window_start_points) > 0:
            candidate_kmers[kmer] = cluster_window_start_points
    
    return candidate_kmers