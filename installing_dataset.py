from datasets import load_dataset


def main():
    # Download IMDb, or reuse it if it is already cached.
    imdb = load_dataset("stanfordnlp/imdb", token=False)

    print("IMDb is ready!")
    print(imdb)

    # Show the local files backing each split.
    for split_name, split in imdb.items():
        print(f"\n{split_name}: {len(split):,} examples")
        for cache_file in split.cache_files:
            print(f"  {cache_file['filename']}")


if __name__ == "__main__":
    main()