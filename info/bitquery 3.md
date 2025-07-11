 1. Общий список монет
 Запрос:
 ```
 query GetActivePumpTradingPairsComplete {
  Solana {
    DEXTradeByTokens(
      where: {
        Trade: {
          Dex: {
            ProtocolFamily: {is: "Raydium"}
          }
          Side: {
            AmountInUSD: {gt: "10000"}
          }
          Currency: {
            MintAddress: {likeCaseInsensitive: "%pump"}
          }
        }
        Block: {
          Time: {since: "2025-06-05T00:00:00Z"}
        }
        Transaction: {
          Result: {Success: true}
        }
      }
      limit: {count: 100}
      orderBy: {descendingByField: "volume"}
    ) {
      Trade {
        Market {
          MarketAddress
        }
        Currency {
          Symbol
          Name
        }
      }
      volume: sum(of: Trade_Side_AmountInUSD)
    }
  }
}
```
Ответ:
```
{
  "Solana": {
    "DEXTradeByTokens": [
      {
        "Trade": {
          "Currency": {
            "Name": "DogeWif",
            "Symbol": "DOGEWIF"
          },
          "Market": {
            "MarketAddress": "7EPew1S4ZdmGfGEi2bCAtyZ9ydHJ1wLBKYsi1FfARPFA"
          }
        },
        "volume": "108839272.46624568"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Wrapped BONK",
            "Symbol": "WBONK"
          },
          "Market": {
            "MarketAddress": "3L35LdYWd7oZDo665mqMD4ZuK7no83gxcad43xj7JLK8"
          }
        },
        "volume": "103496346.82358243"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Pepe House",
            "Symbol": "PHOUSE"
          },
          "Market": {
            "MarketAddress": "DK7RNjuMhW6DxFLif4boXwG891vRZpD6cSz1fUsyJXAK"
          }
        },
        "volume": "89272708.596508"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Pepe Squid",
            "Symbol": "PepeSquid"
          },
          "Market": {
            "MarketAddress": "BY6mTcjAzdPLr8eueuXTQKKuCHCLYmEA1CtwcWWFyhny"
          }
        },
        "volume": "73504610.28181988"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Pepe Trump",
            "Symbol": "PEPETRUMP"
          },
          "Market": {
            "MarketAddress": "Bt9NznxUARVi2kPU8upQrZj8Fmd9JB7XL1zakNfvvsE8"
          }
        },
        "volume": "69542038.83891246"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "moonpepe",
            "Symbol": "moonpepe"
          },
          "Market": {
            "MarketAddress": "AkBFTmidMzou4qE3JTurcjbVzXGU4s1UaHVQ4MU6viKV"
          }
        },
        "volume": "50089675.21331131"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "moontrump",
            "Symbol": "moontrump"
          },
          "Market": {
            "MarketAddress": "EZfyKGMh7JJyZgUrd267hzEd7W84GNh9aHgsCGfeKviW"
          }
        },
        "volume": "47365960.12098914"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "moonpepe",
            "Symbol": "moonpepe"
          },
          "Market": {
            "MarketAddress": "28Ei79oWAjxdCyqwmbQ8FJWQsmoiugM25D2Z6wXAzGCv"
          }
        },
        "volume": "39240989.21210095"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Pepe Sheikh",
            "Symbol": "PEPESH"
          },
          "Market": {
            "MarketAddress": "JAMHqxUmvZALhW77VifbeB4Rp6cEUeptUbhV6ND54c2W"
          }
        },
        "volume": "34592078.68837574"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Fartcoin ",
            "Symbol": "Fartcoin "
          },
          "Market": {
            "MarketAddress": "3MjwoqZHAAbCQLBSn6DtmgL6rpazvgYaxBYGHaxiQYTx"
          }
        },
        "volume": "25588962.497116078"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "AGENDA 47",
            "Symbol": "A47"
          },
          "Market": {
            "MarketAddress": "G59EmU5P85uXYcbPh5JVT6Gz4dYgcd6s6gXvUk6deRJG"
          }
        },
        "volume": "11680326.20716759"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Fartcoin ",
            "Symbol": "Fartcoin "
          },
          "Market": {
            "MarketAddress": "Bzc9NZfMqkXR6fz1DBph7BDf9BroyEf6pnzESP7v5iiw"
          }
        },
        "volume": "11270691.39895325"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Degen Spartan AI",
            "Symbol": "degenai"
          },
          "Market": {
            "MarketAddress": "DLaoh9okkk4gdtXj2mkH3WJUE7VbhMBJRuKmciD1PSZX"
          }
        },
        "volume": "10306338.905676084"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "LABUBU",
            "Symbol": "LABUBU"
          },
          "Market": {
            "MarketAddress": "FYAnFcdjkcfAkbtZqixnTqNVLoDjJft82L5FFgPaSWe3"
          }
        },
        "volume": "7151099.46138104"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "imposter",
            "Symbol": "pump"
          },
          "Market": {
            "MarketAddress": "96dRDoaCqUucZ3wQw6AFqzwq31EMpU6PUbspx8YTKNmg"
          }
        },
        "volume": "5060763.465982401"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Affirm",
            "Symbol": "AFFIRM"
          },
          "Market": {
            "MarketAddress": "CZykxnEiB1qwotBdiorochdPkjDjYQxX2H7N1Mq3jEJs"
          }
        },
        "volume": "2772098.7959382744"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Peanut the Squirrel ",
            "Symbol": "Pnut "
          },
          "Market": {
            "MarketAddress": "4AZRPNEfCJ7iw28rJu5aUyeQhYcvdcNm8cswyL51AY9i"
          }
        },
        "volume": "2681563.4358585645"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Alchemist AI",
            "Symbol": "ALCH"
          },
          "Market": {
            "MarketAddress": "FyDF3vKQFbcvNTsBi7L7LremrFPmXKbQqgAgnPg1hXXd"
          }
        },
        "volume": "2244883.61519391"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "titcoin",
            "Symbol": "titcoin"
          },
          "Market": {
            "MarketAddress": "4qQM2x2pfhU3ToscAqkQxTfhTm7DmJe8LGWU9kvqeNH4"
          }
        },
        "volume": "2134288.124664743"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Cupsey",
            "Symbol": "Cupsey"
          },
          "Market": {
            "MarketAddress": "9U6jGAy5ySvTqjdzc3t7xti7sZnRgGn1wLFKVQnZQuTu"
          }
        },
        "volume": "1717433.19388639"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Fartcoin ",
            "Symbol": "Fartcoin "
          },
          "Market": {
            "MarketAddress": "4sFWHZehgEF5jUXrnaifomJMCp9V1iyp48657f7C6dvv"
          }
        },
        "volume": "1511133.4282206553"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Bertram The Pomeranian",
            "Symbol": "Bert"
          },
          "Market": {
            "MarketAddress": "BmsZE6TkZYskyS1PatPKRyyazGdxWFxdia4BuvLg9AgY"
          }
        },
        "volume": "1502019.4601250924"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Pepe House",
            "Symbol": "PEPEHOUSE"
          },
          "Market": {
            "MarketAddress": "3L2weC6qXNvffpob7LXVDebVTVHPmRBgtG8SxgFwtyGK"
          }
        },
        "volume": "1471599.6077347742"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "DUNA AI",
            "Symbol": "DUNA"
          },
          "Market": {
            "MarketAddress": "6bVqVJzzaWax7wC9YKTf2QyZoqdo9UjxkVDTK1ye9UcS"
          }
        },
        "volume": "1178479.293577404"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Hive AI",
            "Symbol": "BUZZ"
          },
          "Market": {
            "MarketAddress": "J2p6tgZDkvtHQ3VfbGRjzHJNLrqFgGfvjJsp2K7HX5cH"
          }
        },
        "volume": "1161485.283655957"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "OFFICIAL BARRON",
            "Symbol": "BARRON"
          },
          "Market": {
            "MarketAddress": "2ipXWCjR1pgQA57c5LQXhtgegq1D3re4iqbo4zzo9mHV"
          }
        },
        "volume": "944299.5135283938"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Goatseus Μaximus",
            "Symbol": "GΟΑΤ"
          },
          "Market": {
            "MarketAddress": "78SVqjGFBhccegQgA9Nvw5w6HGBXxDTLasBcjDhFDtyT"
          }
        },
        "volume": "940994.8608927571"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "jelly-my-jelly",
            "Symbol": "jellyjelly"
          },
          "Market": {
            "MarketAddress": "3bC2e2RxcfvF9oP22LvbaNsVwoS2T98q6ErCRoayQYdq"
          }
        },
        "volume": "839897.1916649608"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "FWOG",
            "Symbol": "FWOG"
          },
          "Market": {
            "MarketAddress": "AB1eu2L1Jr3nfEft85AuD2zGksUbam1Kr8MR3uM2sjwt"
          }
        },
        "volume": "764563.5107016705"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "The Imposter",
            "Symbol": "PUMP"
          },
          "Market": {
            "MarketAddress": "8TMpieDdUUB2U5V1gFbuSToN5vkTR5HAUwRcZtSShi46"
          }
        },
        "volume": "693558.8074909904"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "DOGE AI",
            "Symbol": "DOGEAI"
          },
          "Market": {
            "MarketAddress": "3d7PRDYq3CvRxFBoXrYeKr3DYYco2AnYupv9D9bAUoyH"
          }
        },
        "volume": "674897.7489922419"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "The Imposter",
            "Symbol": "PUMP"
          },
          "Market": {
            "MarketAddress": "GUcuXbk5zg6VoXdrDXApBAnZnKzHAbVK5Ju5dzDcfQL"
          }
        },
        "volume": "613539.9572773091"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Changeable Milo",
            "Symbol": "Milo"
          },
          "Market": {
            "MarketAddress": "G6uvyMLemfXKT7cLq8YFPmNEfhpmSakEvCaQQesk1qT7"
          }
        },
        "volume": "598155.5191307504"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "MeowCan",
            "Symbol": "MeowCan"
          },
          "Market": {
            "MarketAddress": "Asq3pUTT85nerKD8Xgt8ZAvfGA28f7JivDQWHDu5xBBY"
          }
        },
        "volume": "557733.5591828233"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Fartcoin ",
            "Symbol": "Fartcoin "
          },
          "Market": {
            "MarketAddress": "6U4TBh3aJgiJ5EqCDEua4rP75HsqcfHapMKhhyuTqGuo"
          }
        },
        "volume": "540165.7737920497"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "First Convicted RACCON",
            "Symbol": "FRED"
          },
          "Market": {
            "MarketAddress": "8SQNDszijLRLnXmfQBPzxbBhSUjRJur7CEfqcQZQz1hQ"
          }
        },
        "volume": "537224.6329899073"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Project89",
            "Symbol": "Project89"
          },
          "Market": {
            "MarketAddress": "2yhXxFHiWjWxMiZMsTPRGhiKTWsuYFFx2us2kH8P7Kpq"
          }
        },
        "volume": "525726.857449685"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "AI Rig Complex",
            "Symbol": "arc"
          },
          "Market": {
            "MarketAddress": "J3b6dvheS2Y1cbMtVz5TCWXNegSjJDbUKxdUVDPoqmS7"
          }
        },
        "volume": "474182.2903998082"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "World Liberty Financial",
            "Symbol": "WLFI"
          },
          "Market": {
            "MarketAddress": "9vWVooeqk6udEHyioYr8Lvz6n8VZ45TkgKCtvneEVHCY"
          }
        },
        "volume": "428191.46422763343"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "just buy $1 worth of this coin",
            "Symbol": "$1"
          },
          "Market": {
            "MarketAddress": "HzLxx6SoViXoqB2KYDGT1gWEckZ9ooRnv8n3xN6uvfez"
          }
        },
        "volume": "418368.21985734184"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Just a chill guy",
            "Symbol": "CHILLGUY"
          },
          "Market": {
            "MarketAddress": "93tjgwff5Ac5ThyMi8C4WejVVQq4tuMeMuYW1LEYZ7bu"
          }
        },
        "volume": "393610.5657641867"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "AGENDA 47",
            "Symbol": "A47"
          },
          "Market": {
            "MarketAddress": "CbYweHJeB92Lu7UTiASP3UcGfYPyxhEUjchKf6Yh3fPN"
          }
        },
        "volume": "365849.4871441945"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "nuit",
            "Symbol": "nuit"
          },
          "Market": {
            "MarketAddress": "966sLyXCxj1HedfdFQsv2LiNHUaUhMNadBcD4kDcJ1MP"
          }
        },
        "volume": "352320.3928406285"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "STONKS",
            "Symbol": "STONKS"
          },
          "Market": {
            "MarketAddress": "5N96fYr2ZzaiNyZaYGAi31xvT5ExzfPnwh2s95yaXXSv"
          }
        },
        "volume": "342983.13342567073"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Vine Coin",
            "Symbol": "VINE"
          },
          "Market": {
            "MarketAddress": "58fzJMbX5PatnfJPqWWsqkVFPRKptkbb5r2vCw4Qq3z9"
          }
        },
        "volume": "327105.9067173032"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "BunkerCoin",
            "Symbol": "BUNKER"
          },
          "Market": {
            "MarketAddress": "DwuhdBSzAGvjXJz9k5E3Yp1PbMNdveJCSncHpxEdjv47"
          }
        },
        "volume": "305572.7867857971"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Ava AI",
            "Symbol": "AVA"
          },
          "Market": {
            "MarketAddress": "GjvW8JQSpKG5ogjyD3zozfaeJSShTajS5ZFrexT8L12k"
          }
        },
        "volume": "298495.76285095094"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Slopfather",
            "Symbol": "FATHA"
          },
          "Market": {
            "MarketAddress": "Am1SqWAHhaKWS4H9uwHweeYxCaECR5yDYZiX1jD9RVMP"
          }
        },
        "volume": "286272.23082451615"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Moby AI",
            "Symbol": "MOBY"
          },
          "Market": {
            "MarketAddress": "AemYRZmJryzAQ9Z4RLfUBLnPRUY5ecooc94EJvemfti4"
          }
        },
        "volume": "278890.701231654"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "TOP HAT",
            "Symbol": "HAT"
          },
          "Market": {
            "MarketAddress": "Hoz3sC78FMWSziyyvJuv5kTEamBMSe2j1LUGAMP9SbYU"
          }
        },
        "volume": "278445.5618450367"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "ASTINIA",
            "Symbol": "ASTINIA"
          },
          "Market": {
            "MarketAddress": "EiE1T8nY6k6wHZvsASR7RY4LqZ8CNSprf6Bog9D9y1H7"
          }
        },
        "volume": "264157.14926127886"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Jonathan The Giant Tortoise",
            "Symbol": "JONATHAN"
          },
          "Market": {
            "MarketAddress": "66Q3rfBiUaLjyTowp6YRmPHpBWy3fAAZduVYpBpvvFUg"
          }
        },
        "volume": "263975.5422296395"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "omni",
            "Symbol": "omni"
          },
          "Market": {
            "MarketAddress": "EN9hoyNL2RnryFCVdyeeS3S3j4xaR38R1xw3KbWa9XLx"
          }
        },
        "volume": "252002.8214585025"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "San Chan",
            "Symbol": "San"
          },
          "Market": {
            "MarketAddress": "4BBvrWsocM9wY2qXCCufCL8GxKtNeXT73uNfveK4MMq7"
          }
        },
        "volume": "222116.0655625765"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Shoggoth",
            "Symbol": "Shoggoth"
          },
          "Market": {
            "MarketAddress": "Y8YyWu9gyCYSomE99JkDvsfR4eHNEeQpWtR8quGpBwX"
          }
        },
        "volume": "216996.96681825575"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "opensvm.com",
            "Symbol": "SVMAI"
          },
          "Market": {
            "MarketAddress": "5XSQxHj1ao2YcaiA4m3JJQF3jeXyRjKY5ceKfUf58sT8"
          }
        },
        "volume": "211947.22032028087"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "PWEASE",
            "Symbol": "pwease"
          },
          "Market": {
            "MarketAddress": "9fmdkQipJK2teeUv53BMDXi52uRLbrEvV38K8GBNkiM7"
          }
        },
        "volume": "207328.4340117536"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "The Epstein Files",
            "Symbol": "EPSTEIN"
          },
          "Market": {
            "MarketAddress": "8LCWBRGV8Zieukf8WiTcdQnXNESL41zK74zaASR8gfhe"
          }
        },
        "volume": "206114.55474632705"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "CAUCASIAN CHRISTMAS COIN",
            "Symbol": "CCCOIN "
          },
          "Market": {
            "MarketAddress": "54btkAtaLtnshoyogRmANcaLLoHefbqALiqtjuW6EJo5"
          }
        },
        "volume": "201889.5061597463"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "buidl",
            "Symbol": "buidl"
          },
          "Market": {
            "MarketAddress": "2CotF9J6Q6FMXq9igZmer6iHd6w8pWBD6dtnzMWzNbr3"
          }
        },
        "volume": "198424.26576065752"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "SwarmNode.ai",
            "Symbol": "SNAI"
          },
          "Market": {
            "MarketAddress": "9qiKN1QnuUVtZXhRWo86Prnr3Lsm933MvJ8phrt5ah8Y"
          }
        },
        "volume": "198039.8455251435"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Outfit of the day",
            "Symbol": "OOTD"
          },
          "Market": {
            "MarketAddress": "GeS6WxdSJfUUMQ37WsC75fSRUejCTgXHQikdsVmx8Msu"
          }
        },
        "volume": "193946.84908711197"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "中国数字时代",
            "Symbol": "CDT"
          },
          "Market": {
            "MarketAddress": "GWKgQixtHBkK4hH2PsYimZXG5ezALqotWPPxvktFgGo4"
          }
        },
        "volume": "192801.39587200564"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "FIGHT",
            "Symbol": "FIGHT"
          },
          "Market": {
            "MarketAddress": "A6jBmV67sTtHLHd7uv87VjK8BXjYH515ecWL26HkXUjf"
          }
        },
        "volume": "174261.35364863527"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "pump.fun",
            "Symbol": "pump"
          },
          "Market": {
            "MarketAddress": "8KUNWahYqBYfpHAVDoGayfJtKiYxGjY9c3MLXrRXBfHx"
          }
        },
        "volume": "167210.86165833366"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "RadCoin",
            "Symbol": "RAD"
          },
          "Market": {
            "MarketAddress": "2JnhxBd2BHfgRKNMhr5ojU27BzBHhswdJpypdDXGVf5x"
          }
        },
        "volume": "165885.0727782719"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "swarms",
            "Symbol": "swarms"
          },
          "Market": {
            "MarketAddress": "HL4KFTfhZZMm7NGefszQxzJ3M6CaDWE7TesyuRuQYmMJ"
          }
        },
        "volume": "165589.82951292954"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "AUNTY",
            "Symbol": "AUNTY"
          },
          "Market": {
            "MarketAddress": "5QBX5gmFmgEKhQoiPoBDnPjpy4WWV66GZkizLoTS6gjK"
          }
        },
        "volume": "165462.1668595419"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "SuperToken",
            "Symbol": "SuperToken"
          },
          "Market": {
            "MarketAddress": "H8JaM9JzrN1ezpicscTmf8L2hoy48H9MsyzayiH2couP"
          }
        },
        "volume": "162646.02876014542"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Butthole Coin",
            "Symbol": "Butthole"
          },
          "Market": {
            "MarketAddress": "T5mZpKou42YF3ssrQyrxFJZDL4zvBKg8u1HxqBfDyoo"
          }
        },
        "volume": "162317.01296045133"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "match",
            "Symbol": "match"
          },
          "Market": {
            "MarketAddress": "3HxbQZ21JZW8FCGhfJaaJEWBPYxmJhotEo6eA6Wj3Cys"
          }
        },
        "volume": "160440.6816209042"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Market Dominance",
            "Symbol": "MD"
          },
          "Market": {
            "MarketAddress": "48eKsoi9ZyQU4DbXM9pvcbgsfTxDWqhEVKuGzHAW3ucc"
          }
        },
        "volume": "158664.44251343678"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "/print millions",
            "Symbol": "/print"
          },
          "Market": {
            "MarketAddress": "7PBttiC6A1FWxvm1FUgMVUmyu1BMw7G8Sk6h8knWMgsd"
          }
        },
        "volume": "156683.24960702762"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Italian Brainrot",
            "Symbol": "Italianrot"
          },
          "Market": {
            "MarketAddress": "2baC5JL75NosEr2oLJZ14gbNjWDuUq3ui33ZPLZTgCEA"
          }
        },
        "volume": "155076.0313795691"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "AZIZI",
            "Symbol": "Azizi"
          },
          "Market": {
            "MarketAddress": "2HdRXLTiFZvq4itRL6ii1Drv9ncyV7AwFG32BYhy31iV"
          }
        },
        "volume": "140125.29134057072"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Z̶A̴I̴L̶G̶O̸",
            "Symbol": "ZAILGO"
          },
          "Market": {
            "MarketAddress": "DkNeizAA75GHRhM53obt5ahp45A7hbekdveB99CzVEkN"
          }
        },
        "volume": "139493.84191130652"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "StupidCoin",
            "Symbol": "Stupid"
          },
          "Market": {
            "MarketAddress": "F1FMsNYuCNRHTDVjSkNbiZLp4qv6r6oQyMRJM9ZYdkm3"
          }
        },
        "volume": "137343.64483282925"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "INF",
            "Symbol": "INF"
          },
          "Market": {
            "MarketAddress": "F5pSp1uNJA866qRYuCZUw9KokyWhczH347erBebCtUwq"
          }
        },
        "volume": "134275.7697320052"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Official Elon Coin",
            "Symbol": "ELON"
          },
          "Market": {
            "MarketAddress": "5c4znipkjwGe9PFJay3EswDr3kxAmg2FX1CJsggybEjh"
          }
        },
        "volume": "125366.23731613776"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Bed Hair Cat",
            "Symbol": "tigi"
          },
          "Market": {
            "MarketAddress": "FsQkczpkSEjikmz1DNQtq7KpsJa9zap2iBHwzfLrqpd7"
          }
        },
        "volume": "114074.87873362296"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Goatseus Maximus",
            "Symbol": "GOAT"
          },
          "Market": {
            "MarketAddress": "9Tb2ohu5P16BpBarqd3N27WnkF51Ukfs8Z1GzzLDxVZW"
          }
        },
        "volume": "112661.91316698492"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "BOOP ",
            "Symbol": "BOOP "
          },
          "Market": {
            "MarketAddress": "CZay6UaxdgsCCtCT1qNgWEqCJZ6ekrdHfwumT6bMB3np"
          }
        },
        "volume": "112477.98337261002"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Large Language Model",
            "Symbol": "LLM"
          },
          "Market": {
            "MarketAddress": "G6XZu9m4yAmoW1uGFKcAHUW5ufpURBk4kCeWr9dP1KxJ"
          }
        },
        "volume": "111392.91715657209"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "RETAIL PINK",
            "Symbol": "PINK"
          },
          "Market": {
            "MarketAddress": "6N2yWK4FpeH73G19WToroTocyGPNSKcFuBdQD51skkFQ"
          }
        },
        "volume": "110369.3034655889"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Whilly",
            "Symbol": "Whilly"
          },
          "Market": {
            "MarketAddress": "BZw2mSMYCjhwccwBidYEZrMUz4BZRLbKnKMsAwTwm2n8"
          }
        },
        "volume": "109099.6820111142"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "MANSORY",
            "Symbol": "MNSRY"
          },
          "Market": {
            "MarketAddress": "3ZQPHrpt5QSM1s4V2Ha8nYBgSSsrjLzuEHZeyZjw2af9"
          }
        },
        "volume": "107171.03002053464"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "The Last Play",
            "Symbol": "retire"
          },
          "Market": {
            "MarketAddress": "6HfaJiUuTXFZEfmdkQSNbvfe6i95Nh2wUVJ5dWMf7gtw"
          }
        },
        "volume": "98606.89298395131"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "life changing pill",
            "Symbol": "PILL"
          },
          "Market": {
            "MarketAddress": "FAipE7GQSYqNM4LSB8Fu4MaBctc6ZzeHTPPrL6iXRY5Z"
          }
        },
        "volume": "96571.21441750429"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "gary",
            "Symbol": "GARY"
          },
          "Market": {
            "MarketAddress": "AVicvyigGxNwfWXmz2bTtZX5RN9YTb7QE4qeF46b2mZE"
          }
        },
        "volume": "96491.53491701874"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Never Kill Yourself",
            "Symbol": "Never"
          },
          "Market": {
            "MarketAddress": "2aK5J83cqSyUvRhBbFdWRhZsbUeZ7Cg1U9mwbex5NFKA"
          }
        },
        "volume": "96124.13335892156"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "The tiny chef",
            "Symbol": "Cheffy"
          },
          "Market": {
            "MarketAddress": "AWTbRA6r1MEB9816o4ybT67dLBHAcZrP3Mb8qQsnBC8T"
          }
        },
        "volume": "95036.55223961346"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "vrsus.fun",
            "Symbol": "vrsus"
          },
          "Market": {
            "MarketAddress": "APzD3zNs6phKq5CcULH7XhqQ3EYv57YUbHkyjdS3zSrT"
          }
        },
        "volume": "94751.64328757515"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "ARA",
            "Symbol": "ARA"
          },
          "Market": {
            "MarketAddress": "FdecojaPqw3wavMmscYYmN1Wm53qg5ktG9h7uF9k4xoz"
          }
        },
        "volume": "93345.89281374982"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "PAC AMERICA MASCOT",
            "Symbol": "Trumpie"
          },
          "Market": {
            "MarketAddress": "4uiUyku5koR3hiVbGT56wciEFvtRfGVRddzKf9so1gCn"
          }
        },
        "volume": "93134.81360416656"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "DADDY TATE",
            "Symbol": "DADDY"
          },
          "Market": {
            "MarketAddress": "zcdAw3jpcqEY8JYVxNVMqs2cU35cyDdy4ot7V8edNhz"
          }
        },
        "volume": "92277.92454004374"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "chill cock",
            "Symbol": "CHILLCOCK"
          },
          "Market": {
            "MarketAddress": "DNoHkAMVw7f3CmBCKjCPsMntgJJXt6ka4C45ziqFvAYL"
          }
        },
        "volume": "91696.30102751945"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Wolf",
            "Symbol": "WOLF"
          },
          "Market": {
            "MarketAddress": "5Pce2B55ms8b2uFyptCnVNkPrtzpyKLe5HtMc8UymWxB"
          }
        },
        "volume": "90687.08864546892"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "Comedian",
            "Symbol": "Ban"
          },
          "Market": {
            "MarketAddress": "DmAsjXoceoL5vTKZbYpTpXPo7MKm16FMfNMm3PJFiUha"
          }
        },
        "volume": "89716.69401185826"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "BLORB",
            "Symbol": "BLORB"
          },
          "Market": {
            "MarketAddress": "4hMws864QkFX2kfZBcvmpNmMpuXjYGQopTb3MTDDkyaU"
          }
        },
        "volume": "89675.35536047877"
      },
      {
        "Trade": {
          "Currency": {
            "Name": "TEMU",
            "Symbol": "TEMU"
          },
          "Market": {
            "MarketAddress": "Gu6ek1YQVBtA31Un8QZ5LbSN4qGubcsxoa9LNKvGL8cp"
          }
        },
        "volume": "88970.41199133298"
      }
    ]
  }
}
```
Код:
```
import requests
import json

url = "https://streaming.bitquery.io/eap"

payload = json.dumps({
   "query": "query GetActivePumpTradingPairsComplete {\n  Solana {\n    DEXTradeByTokens(\n      where: {\n        Trade: {\n          Dex: {\n            ProtocolFamily: {is: \"Raydium\"}\n          }\n          Side: {\n            AmountInUSD: {gt: \"10000\"}\n          }\n          Currency: {\n            MintAddress: {likeCaseInsensitive: \"%pump\"}\n          }\n        }\n        Block: {\n          Time: {since: \"2025-06-05T00:00:00Z\"}\n        }\n        Transaction: {\n          Result: {Success: true}\n        }\n      }\n      limit: {count: 100}\n      orderBy: {descendingByField: \"volume\"}\n    ) {\n      Trade {\n        Market {\n          MarketAddress\n        }\n        Currency {\n          Symbol\n          Name\n        }\n      }\n      volume: sum(of: Trade_Side_AmountInUSD)\n    }\n  }\n}",
   "variables": "{}"
})
headers = {
   'Content-Type': 'application/json',
   'Authorization': 'Bearer ory_at_OSwc6vphlYQtFJ_yfv4KRhyZmhxmPgyZDRfekFKSlZ0.84ECLOPa-9IvVPYq288h_v38siQwZPwp-83f33D1deU'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

2. Проверка ликвидности
Запрос:
```
query CheckLiquidityForTokenByMint($tokenAddress: String!) {
  Solana {
    DEXPools(
      where: {
        Pool: {
          Market: {
            BaseCurrency: {
              MintAddress: {is: $tokenAddress}
            }
          }
          Quote: {
            PostAmountInUSD: {gt: "15000"}
          }
        }
        Transaction: {
          Result: {Success: true}
        }
        Block: {
          Time: {since: "2025-07-01T00:00:00Z"}
        }
      }
      limit: {count: 10}
      orderBy: {descendingByField: "Pool_Quote_PostAmountInUSD"}
    ) {
      Pool {
        Market {
          MarketAddress
          BaseCurrency {
            MintAddress
            Symbol
            Name
          }
          QuoteCurrency {
            MintAddress
            Symbol
            Name
          }
        }
        Quote {
          PostAmountInUSD
          PostAmount
        }
        Base {
          PostAmountInUSD
          PostAmount
        }
        Dex {
          ProtocolName
          ProtocolFamily
        }
      }
      Block {
        Time
      }
    }
  }
}
```
Ответ:
```
{
  "Solana": {
    "DEXPools": [
      {
        "Block": {
          "Time": "2025-07-10T07:32:38Z"
        },
        "Pool": {
          "Base": {
            "PostAmount": "2514394.648940",
            "PostAmountInUSD": "28862.945998017392"
          },
          "Dex": {
            "ProtocolFamily": "Meteora",
            "ProtocolName": "lb_clmm"
          },
          "Market": {
            "BaseCurrency": {
              "MintAddress": "DHJVYXsikcimtcVo49FAZqYd1XPYPaXezYhbKArJbonk",
              "Name": "Blue Chip",
              "Symbol": "BlueChip"
            },
            "MarketAddress": "6semcWB5GwzjyqqEYLxd5fPdxX4gNPN5bwDddh124X8K",
            "QuoteCurrency": {
              "MintAddress": "So11111111111111111111111111111111111111112",
              "Name": "Wrapped Solana",
              "Symbol": "WSOL"
            }
          },
          "Quote": {
            "PostAmount": "2102.733651513",
            "PostAmountInUSD": "332761.6109980876"
          }
        }
      },
      {
        "Block": {
          "Time": "2025-07-10T07:30:25Z"
        },
        "Pool": {
          "Base": {
            "PostAmount": "2546074.414979",
            "PostAmountInUSD": "29226.579335063518"
          },
          "Dex": {
            "ProtocolFamily": "Meteora",
            "ProtocolName": "lb_clmm"
          },
          "Market": {
            "BaseCurrency": {
              "MintAddress": "DHJVYXsikcimtcVo49FAZqYd1XPYPaXezYhbKArJbonk",
              "Name": "Blue Chip",
              "Symbol": "BlueChip"
            },
            "MarketAddress": "6semcWB5GwzjyqqEYLxd5fPdxX4gNPN5bwDddh124X8K",
            "QuoteCurrency": {
              "MintAddress": "So11111111111111111111111111111111111111112",
              "Name": "Wrapped Solana",
              "Symbol": "WSOL"
            }
          },
          "Quote": {
            "PostAmount": "2100.419956541",
            "PostAmountInUSD": "332380.1124703822"
          }
        }
      },
      {
        "Block": {
          "Time": "2025-07-10T07:34:12Z"
        },
        "Pool": {
          "Base": {
            "PostAmount": "2514394.648940",
            "PostAmountInUSD": "28862.94833972989"
          },
          "Dex": {
            "ProtocolFamily": "Meteora",
            "ProtocolName": "lb_clmm"
          },
          "Market": {
            "BaseCurrency": {
              "MintAddress": "DHJVYXsikcimtcVo49FAZqYd1XPYPaXezYhbKArJbonk",
              "Name": "Blue Chip",
              "Symbol": "BlueChip"
            },
            "MarketAddress": "6semcWB5GwzjyqqEYLxd5fPdxX4gNPN5bwDddh124X8K",
            "QuoteCurrency": {
              "MintAddress": "So11111111111111111111111111111111111111112",
              "Name": "Wrapped Solana",
              "Symbol": "WSOL"
            }
          },
          "Quote": {
            "PostAmount": "2098.733630681",
            "PostAmountInUSD": "332186.5637541111"
          }
        }
      },
      {
        "Block": {
          "Time": "2025-07-10T07:30:02Z"
        },
        "Pool": {
          "Base": {
            "PostAmount": "2546074.414979",
            "PostAmountInUSD": "29226.579335063518"
          },
          "Dex": {
            "ProtocolFamily": "Meteora",
            "ProtocolName": "lb_clmm"
          },
          "Market": {
            "BaseCurrency": {
              "MintAddress": "DHJVYXsikcimtcVo49FAZqYd1XPYPaXezYhbKArJbonk",
              "Name": "Blue Chip",
              "Symbol": "BlueChip"
            },
            "MarketAddress": "6semcWB5GwzjyqqEYLxd5fPdxX4gNPN5bwDddh124X8K",
            "QuoteCurrency": {
              "MintAddress": "So11111111111111111111111111111111111111112",
              "Name": "Wrapped Solana",
              "Symbol": "WSOL"
            }
          },
          "Quote": {
            "PostAmount": "2098.419956558",
            "PostAmountInUSD": "332063.623276295"
          }
        }
      },
      {
        "Block": {
          "Time": "2025-07-10T07:29:54Z"
        },
        "Pool": {
          "Base": {
            "PostAmount": "2546374.389113",
            "PostAmountInUSD": "29230.022760665786"
          },
          "Dex": {
            "ProtocolFamily": "Meteora",
            "ProtocolName": "lb_clmm"
          },
          "Market": {
            "BaseCurrency": {
              "MintAddress": "DHJVYXsikcimtcVo49FAZqYd1XPYPaXezYhbKArJbonk",
              "Name": "Blue Chip",
              "Symbol": "BlueChip"
            },
            "MarketAddress": "6semcWB5GwzjyqqEYLxd5fPdxX4gNPN5bwDddh124X8K",
            "QuoteCurrency": {
              "MintAddress": "So11111111111111111111111111111111111111112",
              "Name": "Wrapped Solana",
              "Symbol": "WSOL"
            }
          },
          "Quote": {
            "PostAmount": "2098.398048384",
            "PostAmountInUSD": "332060.15642609895"
          }
        }
      },
      {
        "Block": {
          "Time": "2025-07-10T07:29:40Z"
        },
        "Pool": {
          "Base": {
            "PostAmount": "2546374.389113",
            "PostAmountInUSD": "29230.022760665786"
          },
          "Dex": {
            "ProtocolFamily": "Meteora",
            "ProtocolName": "lb_clmm"
          },
          "Market": {
            "BaseCurrency": {
              "MintAddress": "DHJVYXsikcimtcVo49FAZqYd1XPYPaXezYhbKArJbonk",
              "Name": "Blue Chip",
              "Symbol": "BlueChip"
            },
            "MarketAddress": "6semcWB5GwzjyqqEYLxd5fPdxX4gNPN5bwDddh124X8K",
            "QuoteCurrency": {
              "MintAddress": "So11111111111111111111111111111111111111112",
              "Name": "Wrapped Solana",
              "Symbol": "WSOL"
            }
          },
          "Quote": {
            "PostAmount": "2097.398048400",
            "PostAmountInUSD": "331901.91183024214"
          }
        }
      },
      {
        "Block": {
          "Time": "2025-07-10T07:29:38Z"
        },
        "Pool": {
          "Base": {
            "PostAmount": "2546374.389113",
            "PostAmountInUSD": "29230.022760665786"
          },
          "Dex": {
            "ProtocolFamily": "Meteora",
            "ProtocolName": "lb_clmm"
          },
          "Market": {
            "BaseCurrency": {
              "MintAddress": "DHJVYXsikcimtcVo49FAZqYd1XPYPaXezYhbKArJbonk",
              "Name": "Blue Chip",
              "Symbol": "BlueChip"
            },
            "MarketAddress": "6semcWB5GwzjyqqEYLxd5fPdxX4gNPN5bwDddh124X8K",
            "QuoteCurrency": {
              "MintAddress": "So11111111111111111111111111111111111111112",
              "Name": "Wrapped Solana",
              "Symbol": "WSOL"
            }
          },
          "Quote": {
            "PostAmount": "2096.962176400",
            "PostAmountInUSD": "331832.9374406533"
          }
        }
      },
      {
        "Block": {
          "Time": "2025-07-10T07:25:09Z"
        },
        "Pool": {
          "Base": {
            "PostAmount": "2571508.545396",
            "PostAmountInUSD": "28382.42592800729"
          },
          "Dex": {
            "ProtocolFamily": "Meteora",
            "ProtocolName": "lb_clmm"
          },
          "Market": {
            "BaseCurrency": {
              "MintAddress": "DHJVYXsikcimtcVo49FAZqYd1XPYPaXezYhbKArJbonk",
              "Name": "Blue Chip",
              "Symbol": "BlueChip"
            },
            "MarketAddress": "6semcWB5GwzjyqqEYLxd5fPdxX4gNPN5bwDddh124X8K",
            "QuoteCurrency": {
              "MintAddress": "So11111111111111111111111111111111111111112",
              "Name": "Wrapped Solana",
              "Symbol": "WSOL"
            }
          },
          "Quote": {
            "PostAmount": "2096.166623636",
            "PostAmountInUSD": "331803.5121654965"
          }
        }
      },
      {
        "Block": {
          "Time": "2025-07-10T07:23:13Z"
        },
        "Pool": {
          "Base": {
            "PostAmount": "2575606.835785",
            "PostAmountInUSD": "28427.715023086894"
          },
          "Dex": {
            "ProtocolFamily": "Meteora",
            "ProtocolName": "lb_clmm"
          },
          "Market": {
            "BaseCurrency": {
              "MintAddress": "DHJVYXsikcimtcVo49FAZqYd1XPYPaXezYhbKArJbonk",
              "Name": "Blue Chip",
              "Symbol": "BlueChip"
            },
            "MarketAddress": "6semcWB5GwzjyqqEYLxd5fPdxX4gNPN5bwDddh124X8K",
            "QuoteCurrency": {
              "MintAddress": "So11111111111111111111111111111111111111112",
              "Name": "Wrapped Solana",
              "Symbol": "WSOL"
            }
          },
          "Quote": {
            "PostAmount": "2095.866623636",
            "PostAmountInUSD": "331791.8110325596"
          }
        }
      },
      {
        "Block": {
          "Time": "2025-07-10T07:24:42Z"
        },
        "Pool": {
          "Base": {
            "PostAmount": "2575606.835785",
            "PostAmountInUSD": "28427.659852508732"
          },
          "Dex": {
            "ProtocolFamily": "Meteora",
            "ProtocolName": "lb_clmm"
          },
          "Market": {
            "BaseCurrency": {
              "MintAddress": "DHJVYXsikcimtcVo49FAZqYd1XPYPaXezYhbKArJbonk",
              "Name": "Blue Chip",
              "Symbol": "BlueChip"
            },
            "MarketAddress": "6semcWB5GwzjyqqEYLxd5fPdxX4gNPN5bwDddh124X8K",
            "QuoteCurrency": {
              "MintAddress": "So11111111111111111111111111111111111111112",
              "Name": "Wrapped Solana",
              "Symbol": "WSOL"
            }
          },
          "Quote": {
            "PostAmount": "2095.866623636",
            "PostAmountInUSD": "331756.0249798275"
          }
        }
      }
    ]
  }
}
```
Код:
```
import requests
import json

url = "https://streaming.bitquery.io/eap"

payload = json.dumps({
   "query": "query CheckLiquidityForTokenByMint($tokenAddress: String!) {\n  Solana {\n    DEXPools(\n      where: {\n        Pool: {\n          Market: {\n            BaseCurrency: {\n              MintAddress: {is: $tokenAddress}\n            }\n          }\n          Quote: {\n            PostAmountInUSD: {gt: \"15000\"}\n          }\n        }\n        Transaction: {\n          Result: {Success: true}\n        }\n        Block: {\n          Time: {since: \"2025-07-01T00:00:00Z\"}\n        }\n      }\n      limit: {count: 10}\n      orderBy: {descendingByField: \"Pool_Quote_PostAmountInUSD\"}\n    ) {\n      Pool {\n        Market {\n          MarketAddress\n          BaseCurrency {\n            MintAddress\n            Symbol\n            Name\n          }\n          QuoteCurrency {\n            MintAddress\n            Symbol\n            Name\n          }\n        }\n        Quote {\n          PostAmountInUSD\n          PostAmount\n        }\n        Base {\n          PostAmountInUSD\n          PostAmount\n        }\n        Dex {\n          ProtocolName\n          ProtocolFamily\n        }\n      }\n      Block {\n        Time\n      }\n    }\n  }\n}",
   "variables": "{\"tokenAddress\": \"DHJVYXsikcimtcVo49FAZqYd1XPYPaXezYhbKArJbonk\"}"
})
headers = {
   'Content-Type': 'application/json',
   'Authorization': 'Bearer ory_at_OSwc6vphlYQtFJ_yfv4KRhyZmhxmPgyZDRfekFKSlZ0.84ECLOPa-9IvVPYq288h_v38siQwZPwp-83f33D1deU'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

3. Дневная история цен
Запрос:
```
query GetDailyOHLCFixed {
  Solana(dataset: combined) {
    DEXTradeByTokens(
      orderBy: {ascendingByField: "Block_Timefield"}
      where: {
        Trade: {
          Currency: {
            MintAddress: {is: "DHJVYXsikcimtcVo49FAZqYd1XPYPaXezYhbKArJbonk"}
          }
          Side: {
            Currency: {
              MintAddress: {is: "So11111111111111111111111111111111111111112"}
            }
          }
          PriceInUSD: {gt: 0}
        }
        Block: {
          Time: {since: "2025-01-01T00:00:00Z"}
        }
        Transaction: {
          Result: {Success: true}
        }
      }
      limit: {count: 300}
    ) {
      Block {
        Timefield: Time(interval: {count: 1, in: days})
      }
      volume: sum(of: Trade_Amount)
      volumeUSD: sum(of: Trade_Side_AmountInUSD)
      Trade {
        high: PriceInUSD(maximum: Trade_PriceInUSD)
        low: PriceInUSD(minimum: Trade_PriceInUSD)
        open: PriceInUSD(minimum: Block_Slot)
        close: PriceInUSD(maximum: Block_Slot)
      }
      count
    }
  }
}
```
Ответ:
```
{
  "Solana": {
    "DEXTradeByTokens": [
      {
        "Block": {
          "Timefield": "2025-06-25T00:00:00Z"
        },
        "Trade": {
          "close": 0.000038525699766304765,
          "high": 0.0012502014412027536,
          "low": 0.000004375158890356459,
          "open": 0.000004375158890356459
        },
        "count": "17507",
        "volume": "19451166559.323059",
        "volumeUSD": "1908493.6868312403"
      },
      {
        "Block": {
          "Timefield": "2025-06-26T00:00:00Z"
        },
        "Trade": {
          "close": 0.000008197272183066026,
          "high": 0.0000505099221549525,
          "low": 0.000007396335399094754,
          "open": 0.00003729869326648986
        },
        "count": "1611",
        "volume": "3587839501.316290",
        "volumeUSD": "83257.4861913088"
      },
      {
        "Block": {
          "Timefield": "2025-06-27T00:00:00Z"
        },
        "Trade": {
          "close": 0.0000054278174960052,
          "high": 0.00000829621698456552,
          "low": 0.000005427529321164537,
          "open": 0.00000829621698456552
        },
        "count": "128",
        "volume": "469717190.575746",
        "volumeUSD": "3096.744500911581"
      },
      {
        "Block": {
          "Timefield": "2025-06-28T00:00:00Z"
        },
        "Trade": {
          "close": 0.00001687577411244141,
          "high": 0.0000387165179633353,
          "low": 0.00000588827764953443,
          "open": 0.00000588827764953443
        },
        "count": "517",
        "volume": "2237496511.995495",
        "volumeUSD": "37025.06040318754"
      },
      {
        "Block": {
          "Timefield": "2025-06-29T00:00:00Z"
        },
        "Trade": {
          "close": 0.000011302890423692014,
          "high": 0.0000177567799134781,
          "low": 0.000010743552792841413,
          "open": 0.000017237640599239864
        },
        "count": "208",
        "volume": "676635106.623431",
        "volumeUSD": "9396.05376984912"
      },
      {
        "Block": {
          "Timefield": "2025-06-30T00:00:00Z"
        },
        "Trade": {
          "close": 0.00013689451991173973,
          "high": 0.00018483635999992643,
          "low": 0.000010451579253043118,
          "open": 0.000011409544867408239
        },
        "count": "746",
        "volume": "2784684959.744819",
        "volumeUSD": "143189.8278917417"
      },
      {
        "Block": {
          "Timefield": "2025-07-01T00:00:00Z"
        },
        "Trade": {
          "close": 0.003861572793099644,
          "high": 0.005699344040897961,
          "low": 0.00010752377272665894,
          "open": 0.0001316641717705215
        },
        "count": "22099",
        "volume": "5646969265.518979",
        "volumeUSD": "5279262.116799758"
      },
      {
        "Block": {
          "Timefield": "2025-07-02T00:00:00Z"
        },
        "Trade": {
          "close": 0.0036118550230639416,
          "high": 0.00826983402295785,
          "low": 0.001748167200959561,
          "open": 0.004013781506513698
        },
        "count": "40872",
        "volume": "1933340781.971712",
        "volumeUSD": "9582300.718535434"
      },
      {
        "Block": {
          "Timefield": "2025-07-03T00:00:00Z"
        },
        "Trade": {
          "close": 0.005396693284881617,
          "high": 0.008662205886448341,
          "low": 0.0022520648987710374,
          "open": 0.003614908250314325
        },
        "count": "25494",
        "volume": "1441406233.012770",
        "volumeUSD": "7235031.360989729"
      },
      {
        "Block": {
          "Timefield": "2025-07-04T00:00:00Z"
        },
        "Trade": {
          "close": 0.009096627301622801,
          "high": 0.010959627941501793,
          "low": 0.004470111731326941,
          "open": 0.0052243680520775385
        },
        "count": "18575",
        "volume": "614457568.835747",
        "volumeUSD": "4420569.423118852"
      },
      {
        "Block": {
          "Timefield": "2025-07-05T00:00:00Z"
        },
        "Trade": {
          "close": 0.008922628050087885,
          "high": 0.013325779200452248,
          "low": 0.005090560913085938,
          "open": 0.009101972343640437
        },
        "count": "17776",
        "volume": "408870260.025907",
        "volumeUSD": "4195064.345500201"
      },
      {
        "Block": {
          "Timefield": "2025-07-06T00:00:00Z"
        },
        "Trade": {
          "close": 0.0065468182021924,
          "high": 0.011003126077007765,
          "low": 0.005628647415726273,
          "open": 0.009185376625455667
        },
        "count": "14461",
        "volume": "523150106.650140",
        "volumeUSD": "3959567.5884443703"
      },
      {
        "Block": {
          "Timefield": "2025-07-07T00:00:00Z"
        },
        "Trade": {
          "close": 0.00922122612812798,
          "high": 0.011315105800830096,
          "low": 0.005147836882704111,
          "open": 0.006410085298643247
        },
        "count": "17854",
        "volume": "587709119.071281",
        "volumeUSD": "4023793.1478957823"
      },
      {
        "Block": {
          "Timefield": "2025-07-08T00:00:00Z"
        },
        "Trade": {
          "close": 0.00845366919220479,
          "high": 0.012590136885601495,
          "low": 0.006125407095819849,
          "open": 0.009417969957436644
        },
        "count": "19189",
        "volume": "562206320.312133",
        "volumeUSD": "4791159.8034347"
      },
      {
        "Block": {
          "Timefield": "2025-07-09T00:00:00Z"
        },
        "Trade": {
          "close": 0.008486368281037703,
          "high": 0.012845859097135669,
          "low": 0.008245371400102893,
          "open": 0.008747760071195284
        },
        "count": "12584",
        "volume": "312097966.763843",
        "volumeUSD": "3043307.1393762543"
      },
      {
        "Block": {
          "Timefield": "2025-07-10T00:00:00Z"
        },
        "Trade": {
          "close": 0.01062798034815164,
          "high": 0.013002859019406102,
          "low": 0.008338737086245888,
          "open": 0.008516028187596307
        },
        "count": "3550",
        "volume": "100690534.072813",
        "volumeUSD": "1036032.1472840942"
      }
    ]
  }
}
```
Код:
```
import requests
import json

url = "https://streaming.bitquery.io/eap"

payload = json.dumps({
   "query": "query GetDailyOHLCFixed {\n  Solana(dataset: combined) {\n    DEXTradeByTokens(\n      orderBy: {ascendingByField: \"Block_Timefield\"}\n      where: {\n        Trade: {\n          Currency: {\n            MintAddress: {is: \"DHJVYXsikcimtcVo49FAZqYd1XPYPaXezYhbKArJbonk\"}\n          }\n          Side: {\n            Currency: {\n              MintAddress: {is: \"So11111111111111111111111111111111111111112\"}\n            }\n          }\n          PriceInUSD: {gt: 0}\n        }\n        Block: {\n          Time: {since: \"2025-01-01T00:00:00Z\"}\n        }\n        Transaction: {\n          Result: {Success: true}\n        }\n      }\n      limit: {count: 300}\n    ) {\n      Block {\n        Timefield: Time(interval: {count: 1, in: days})\n      }\n      volume: sum(of: Trade_Amount)\n      volumeUSD: sum(of: Trade_Side_AmountInUSD)\n      Trade {\n        high: PriceInUSD(maximum: Trade_PriceInUSD)\n        low: PriceInUSD(minimum: Trade_PriceInUSD)\n        open: PriceInUSD(minimum: Block_Slot)\n        close: PriceInUSD(maximum: Block_Slot)\n      }\n      count\n    }\n  }\n}",
   "variables": "{}"
})
headers = {
   'Content-Type': 'application/json',
   'Authorization': 'Bearer ory_at_OSwc6vphlYQtFJ_yfv4KRhyZmhxmPgyZDRfekFKSlZ0.84ECLOPa-9IvVPYq288h_v38siQwZPwp-83f33D1deU'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```
