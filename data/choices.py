# Define the possible solicitation types

PRESOLICITATION = 'PRESOL'
COMBINED = 'COMB'
SOURCESSOUGHT = 'SS'
MODIFICATION = 'MOD'
SURPLUS = 'SUR'
SPECIALNOTICE = 'NOTICE'
FOREIGNSTANDARD = 'FORGOVSTD'
AWARDNOTICE = 'AWDNTC'
JUSTIFICATION = 'JST'
INTENTTOBUNDLE = 'BUNDLE'
FAIROPPORTUNITY = 'FAIR'
SOLICITATION_TYPES = (
    (PRESOLICITATION, 'Pre-Solicitation'),
    (COMBINED, 'Combined Synopsis/Solicitation'),
    (SOURCESSOUGHT, 'Sources Sought'),
    (MODIFICATION, 'Modification/Amendment/Cancel'),
    (SURPLUS, 'Sale of Surplus Property'),
    (SPECIALNOTICE, 'Special Notice'),
    (FOREIGNSTANDARD, 'Foreign Government Standard'),
    (AWARDNOTICE, 'Award Notice'),
    (JUSTIFICATION, 'Justification and Approval'),
    (INTENTTOBUNDLE, 'Intent to Bundle Requirements'),
    (FAIROPPORTUNITY, 'Fair Opportunity / Limited Sources Justification'),
)