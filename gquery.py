from gql import gql


def get_bosses():
    query = gql(
        """
    query GetBosses {
        bosses {
            name
            normalizedName
            imagePortraitLink
            health {
                max
            }
            equipment {
                item {
                    id
                    containsItems {
                        item {
                            id
                        }
                    }
                }
            }
            items {
                id
            }
        }
    }"""
    )
    return query


def get_items():
    query = gql(
        """query StashItems {
        items {
            id
            name
            shortName
            normalizedName
            updated
            width
            height
            weight
            iconLink
            link
            category {
                name
                id
            }
            properties {
                ...on ItemPropertiesAmmo {
                    caliber
                    penetrationPower
                    damage
                    armorDamage
                    fragmentationChance
                    initialSpeed
                }
                ...on ItemPropertiesStim {
                    cures
                    stimEffects {
                        type
                        chance
                        delay
                        duration
                        value
                        percent
                        skillName
                    }
                }
                ...on ItemPropertiesWeapon {
                    defaultPreset {
                        iconLink
                        width
                        height
                        traderPrices {
                            price
                            priceRUB
                            currency
                            trader {
                                id
                                name
                            }
                        }
                        sellFor {
                            price
                            currency
                            priceRUB
                            vendor {
                                name
                                normalizedName
                                ...on TraderOffer {
                                    trader {
                                        id
                                    }
                                }
                            }
                        }
                    }
                }
            }
            avg24hPrice
            lastLowPrice
            traderPrices {
                price
                priceRUB
                currency
                trader {
                    id
                    name
                }
            }
            buyFor {
                price
                currency
                priceRUB
                vendor {
                    name
                    ...on TraderOffer {
                        trader {
                            id
                        }
                        minTraderLevel
                        taskUnlock {
                            id
                        }
                    }
                }
            }
            sellFor {
                price
                currency
                priceRUB
                vendor {
                    name
                    ...on TraderOffer {
                        trader {
                            id
                        }
                    }
                }
            }
            types
            basePrice
            craftsFor {
                id
            }
            craftsUsing {
                id
            }
            bartersFor {
                id
            }
            bartersUsing {
                id
            }
        }
    }"""
    )
    return query


def get_maps():
    query = gql(
        """query StashMaps {
        maps {
            id
            tarkovDataId
            name
            normalizedName
            wiki
            description
            enemies
            raidDuration
            players
            bosses {
                name
                normalizedName
                spawnChance
                spawnLocations {
                    name
                    chance
                }
                escorts {
                    name
                    normalizedName
                    amount {
                        count
                        chance
                    }
                }
                spawnTime
                spawnTimeRandom
                spawnTrigger
            }
            accessKeys {
                id
            }
            accessKeysMinPlayerLevel
            }
        }"""
    )
    return query


def get_traders():
    query = gql(
        """
        query Traders{
            traders{
                id
                tarkovDataId
                name
                normalizedName
                resetTime
                discount
                levels {
                    id
                    level
                    payRate
                }
            }
        }  
            """
    )
    return query


def get_hideout():
    query = gql(
        """
        query Hideout {
            hideoutStations {
                id
                tarkovDataId
                name
                levels {
                    id
                    tarkovDataId
                    level
                }
            }
        }"""
    )
    return query


def get_flea():
    query = gql(
        """
                query flea {
                    fleaMarket {
                    minPlayerLevel
                    enabled
                    sellOfferFeeRate
                    sellRequirementFeeRate
                }
            }
            """
    )
    return query


def get_barters():
    query = gql(
        """
        query StashBarters {
            barters {
                id
                trader {
                    id
                }
                level
                taskUnlock {
                    id
                }
                requiredItems {
                    item {
                        id
                    }
                    attributes {
                        name
                        value
                    }
                    count
                }
                rewardItems {
                    item {
                        id
                    }
                    count
                }
            }
        }
    """
    )
    return query


def get_crafts():
    query = gql(
        """query StashCrafts {
        crafts {
            id
            station {
                id
            }
            level
            duration
            requiredItems {
                item {
                    id
                }
                count
                attributes {
                    type
                    value
                }
            }
            rewardItems {
                item {
                    id
                }
                count
            }
        }
    }"""
    )
    return query


maps = (
    "https://raw.githubusercontent.com/the-hideout/tarkov-dev/master/src/data/maps.json"
)
