tdev_queries = {
    "barters": """
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
    """,
    "bosses": """
        query Bosses {
            bosses {
                id
                name
                normalizedName
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
        }
        """,
    "crafts": """
            query Crafts {
                crafts {
                    id
                    station {
                        id
                        name
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
            }
            """,
    "hideout": """
        query Hideout {
            hideoutStations {
                id
                tarkovDataId
                name
                levels {
                    id
                    tarkovDataId
                    level
                    constructionTime
                    itemRequirements {
                        id
                        item {
                            id
                            name
                        }
                        count
                        quantity
                    }
                    stationLevelRequirements {
                        id
                        station {
                            id
                            name
                        }
                        level
                    }
                    skillRequirements {
                        name
                        level
                    }
                    traderRequirements {
                        id
                        trader {
                            id
                            name
                        }
                        requirementType
                        compareMethod
                        value
                    }
                }
            }
        }
        """,
    "items": """
        query StashItems {
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
                    stackMaxSize
                    tracer
                    tracerColor
                    ammoType
                    projectileCount
                    penetrationPower
                    damage
                    armorDamage
                    fragmentationChance
                    initialSpeed
                    ricochetChance
                    penetrationChance
                    accuracyModifier
                    recoilModifier
                    lightBleedModifier
                    heavyBleedModifier
                    durabilityBurnFactor
                    heatFactor
                    staminaBurnPerDamage
                    ballisticCoeficient
                    bulletDiameterMilimeters
                    bulletMassGrams

                }
                ...on ItemPropertiesStim{
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
                ...on ItemPropertiesWeapon{
                    caliber
                    defaultAmmo {
                        id
                        name
                    }
                    effectiveDistance
                    ergonomics
                    fireModes
                    fireRate
                    maxDurability
                    recoilVertical
                    recoilHorizontal
                    repairCost
                    sightingRange
                    centerOfImpact
                    deviationCurve
                    recoilDispersion
                    recoilAngle
                    cameraRecoil
                    cameraSnap
                    deviationMax
                    convergence
                    defaultWidth
                    defaultHeight
                    defaultErgonomics
                    defaultRecoilVertical
                    defaultRecoilHorizontal
                    defaultWeight
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
    }
    """,
    "maps": """
        query Maps {
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
                    boss {
                        id
                        name
                    }
                }
                nameId
                accessKeys {
                    id
                    name
                }
                accessKeysMinPlayerLevel
                spawns {
                    zoneName
                    position {
                        x
                        y
                        z
                    }
                    sides
                    categories
                }
                extracts {
                    id
                    name
                    faction
                    switches {
                        id
                        name
                        switchType
                        activatedBy {
                            id
                            name
                        }
                        activates{
                            operation
                            target {
                                ...on MapSwitch {
                                    id
                                    name
                                }
                                ...on MapExtract {
                                    id
                                    name
                                }
                            }
                        }
                    }
                }
                locks {
                    lockType
                    key {
                        id
                        name
                    }
                    needsPower
                    position {
                        x
                        y
                        z
                    }
                }
                switches {
                    id
                    name
                    switchType
                    activatedBy {
                        id
                        name
                    }
                    activates{
                        operation
                        target {
                            ...on MapSwitch {
                                id
                                name
                            }
                            ...on MapExtract {
                                id
                                name
                            }
                        }
                    }
                }
                hazards {
                    hazardType
                    name
                    position {
                        x
                        y
                        z
                    }
                }
                lootContainers {
                    lootContainer {
                        id
                        name
                        normalizedName
                    }
                    position {
                        x
                        y
                        z
                    }
                }
                stationaryWeapons {
                    stationaryWeapon {
                        id
                        name
                        shortName
                    }
                    position {
                        x
                        y
                        z
                    }
                }

            }
        }
        """,
    "tasks": """
        query Tasks {
            tasks {
                id
                tarkovDataId
                name
                normalizedName
                trader {
                    id
                    name
                }
                map {
                    id
                    name
                }
                experience
                wikiLink
                minPlayerLevel
                taskRequirements {
                    task {
                        id
                        name
                    }
                    status
                }
                traderRequirements {
                    id
                    trader {
                        id
                        name
                    }
                    requirementType
                    compareMethod
                    value
                }
                objectives {
                    id
                    type
                    description
                    maps {
                        id
                        name
                    }
                    optional
                }
                startRewards {
                    traderStanding {
                        trader {
                            id
                            name
                        }
                        standing
                    }
                    items {
                        item {
                            id
                            name
                        }
                        count
                        quantity
                    }
                    offerUnlock {
                        id
                        trader {
                            id
                            name
                        }
                        level
                        item {
                            id
                            name
                        }
                    }
                    skillLevelReward {
                        name
                        level
                    }
                    traderUnlock {
                        id
                        name
                    }
                    craftUnlock {
                        id
                    }
                }
                finishRewards {
                    traderStanding {
                        trader {
                            id
                            name
                        }
                        standing
                    }
                    items {
                        item {
                            id
                            name
                        }
                        count
                        quantity
                    }
                    offerUnlock {
                        id
                        trader {
                            id
                            name
                        }
                        level
                        item {
                            id
                            name
                        }
                    }
                    skillLevelReward {
                        name
                        level
                    }
                    traderUnlock {
                        id
                        name
                    }
                    craftUnlock {
                        id
                    }
                }
                failConditions {
                    id
                    type
                    description
                    maps {
                        id
                        name
                    }
                    optional
                }
                failureOutcome {
                    traderStanding {
                        trader {
                            id
                            name
                        }
                        standing
                    }
                    items {
                        item {
                            id
                            name
                        }
                        count
                        quantity
                    }
                    offerUnlock {
                        id
                        trader {
                            id
                            name
                        }
                        level
                        item {
                            id
                            name
                        }
                    }
                    skillLevelReward {
                        name
                        level
                    }
                    traderUnlock {
                        id
                        name
                    }
                    craftUnlock {
                        id
                    }
                }
                restartable
                factionName
                kappaRequired
                lightkeeperRequired

            }
        }
        """,
    "traders": """
        query Traders {
            traders {
                id
                name
                normalizedName
                description
                resetTime
                currency {
                    name
                }
                discount
                levels {
                    id
                    level
                    requiredPlayerLevel
                    requiredReputation
                    requiredCommerce
                    payRate
                    insuranceRate
                    repairCostMultiplier
                    barters {
                        id
                    }
                    cashOffers {
                        item {
                            id
                            name
                        }
                    }
                }
                reputationLevels {
                    ...on TraderReputationLevelFence {
                        minimumReputation
                        scavCooldownModifier
                        scavCaseTimeModifier
                        extractPriceModifier
                        scavFollowChance
                        scavEquipmentSpawnChanceModifier
                        priceModifier
                        hostileBosses
                        hostileScavs
                        scavAttackSupport
                        availableScavExtracts
                        btrEnabled
                        btrDeliveryDiscount
                        btrDeliveryGridSize {
                            x
                            y
                            z
                        }
                        btrTaxiDiscount
                        btrCoveringFireDiscount
                    }
                }
                barters {
                    id
                }
                cashOffers {
                    item {
                        id
                        name
                    }
                    minTraderLevel
                    price
                    currency
                    currencyItem {
                        id
                        name
                    }
                    priceRUB
                    taskUnlock {
                        id
                    }
                }
                tarkovDataId
            }
        }
    """,
    "flea": """
        query Flea {
            fleaMarket {
                name
                normalizedName
                minPlayerLevel
                enabled
                sellOfferFeeRate
                sellRequirementFeeRate
                reputationLevels {
                    offers
                    minRep
                    maxRep
                }
            }
        }
    """,
}

maps = (
    "https://raw.githubusercontent.com/the-hideout/tarkov-dev/master/src/data/maps.json"
)


def update(field="all"):
    if field == "all":
        return tdev_queries
    try:
        return tdev_queries[field]
    except IndexError:
        return None
