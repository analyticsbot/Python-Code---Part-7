# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RealcommercialItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    dateCrawled = scrapy.Field()
    source = scrapy.Field()
    PageTitle = scrapy.Field()
    DisplayablePrice = scrapy.Field()
    PropertyDetailsUrl = scrapy.Field()
    ConjunctionalAgencyBannerURL = scrapy.Field()
    OccupancyStatus = scrapy.Field()
    ConjunctionalAgencyContactPhone = scrapy.Field()
    ParkingOptions = scrapy.Field()
    DisplayableAddressStreet = scrapy.Field()
    Suburb = scrapy.Field()
    DateFirstListed = scrapy.Field()
    SaleID = scrapy.Field()
    EoiRecipientName = scrapy.Field()
    AgencyBannerUrlCre = scrapy.Field()
    HasInspections = scrapy.Field()
    PropertyWebLink = scrapy.Field()
    EoiDeliveryAddress = scrapy.Field()
    CardType = scrapy.Field()
    Inspections = scrapy.Field()
    Availability = scrapy.Field()
    State = scrapy.Field()
    TenderDeliveryAddress = scrapy.Field()
    Type = scrapy.Field()
    AgencyAddress = scrapy.Field()
    LeaseListingUrl = scrapy.Field()
    InspectionTime = scrapy.Field()
    ConjunctionalAgencyId = scrapy.Field()
    DisplayableAddressSuburb = scrapy.Field()
    Categories = scrapy.Field()
    Postcode = scrapy.Field()
    AuctionDate = scrapy.Field()
    AgencyLogoURLCRE = scrapy.Field()
    VideoURL = scrapy.Field()
    ConjunctionAgency = scrapy.Field()
    ListingCategory = scrapy.Field()
    BuildingType = scrapy.Field()
    TenderEndDateAndTime = scrapy.Field()
    ConjunctionalAgencyLogoLargeURL = scrapy.Field()
    LeaseEndDate = scrapy.Field()
    CaptionType = scrapy.Field()
    LastUpdated = scrapy.Field()
    BrandingBannerUrl = scrapy.Field()
    AgencyId = scrapy.Field()
    AgencyName = scrapy.Field()
    PrimaryAgencyColor = scrapy.Field()
    Address = scrapy.Field()
    ListingContacts = scrapy.Field()
    LogoUrl = scrapy.Field()
    PriceDisplayText = scrapy.Field()
    AdID = scrapy.Field()
    Images = scrapy.Field()
    BuildArea = scrapy.Field()
    MapLongitude = scrapy.Field()
    LeaseStartDate = scrapy.Field()
    DisplayAddressType = scrapy.Field()
    AgencyLogoLargeURLCRE = scrapy.Field()
    TenantName = scrapy.Field()
    UnitDetails = scrapy.Field()
    DatePlatinumBilling = scrapy.Field()
    AnnualReturn = scrapy.Field()
    AuctionAddress = scrapy.Field()
    VideoInfo = scrapy.Field()
    LeaseOptions = scrapy.Field()
    LandArea = scrapy.Field()
    DisplayableAddressTruncated = scrapy.Field()
    SaleType = scrapy.Field()
    ConjunctionalAgencyAddress = scrapy.Field()
    AuctionTerms = scrapy.Field()
    NabersRating = scrapy.Field()
    TenantInformation = scrapy.Field()
    IsArchived = scrapy.Field()
    TenderRecipientName = scrapy.Field()
    EoiEndDateAndTime = scrapy.Field()
    Parking = scrapy.Field()
    PrimaryImageFullSizeUrl = scrapy.Field()
    Headline = scrapy.Field()
    MapLatitude = scrapy.Field()
    ConjunctionalAgencyName = scrapy.Field()
    AdFormat = scrapy.Field()
    Description = scrapy.Field()
    BuildOrLandArea = scrapy.Field()
    EoiEndDate = scrapy.Field()
    VirtualTourUrl = scrapy.Field()
    PdfUploads = scrapy.Field()
    RentID = scrapy.Field()
    ConjunctionalAgencyContactName = scrapy.Field()
    TypeString = scrapy.Field()
    ResultItemName = scrapy.Field()
    BreadCrumbItems = scrapy.Field()
    DateUpdated = scrapy.Field()
    FirstPropertyTypeName = scrapy.Field()
    DateEliteBilling = scrapy.Field()
    TenantRentDetail = scrapy.Field()
    SaleListingUrl = scrapy.Field()
    ConjunctionalAgencyLogoURL = scrapy.Field()
    DisplayableAddress = scrapy.Field()
    PageID = scrapy.Field()
    TitanContentType = scrapy.Field()
    IsSPA = scrapy.Field()
    TitanAdZone = scrapy.Field()
    ctype = scrapy.Field()
    Member = scrapy.Field()
    SubCategory4 = scrapy.Field()
    SubCategory2 = scrapy.Field()
    SubCategory3 = scrapy.Field()
    SubCategory1 = scrapy.Field()
    PageName = scrapy.Field()
    PageType = scrapy.Field()
    PageDescription = scrapy.Field()
    IsTitanEnabled = scrapy.Field()
    PrimaryCategory = scrapy.Field()
    AdSlots = scrapy.Field()
    startDate = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    sameAs = scrapy.Field()
    context = scrapy.Field()
    addressLocality = scrapy.Field()
    addressRegion = scrapy.Field()
    streetAddress = scrapy.Field()
    postalCode = scrapy.Field()
    type = scrapy.Field()
    description = scrapy.Field()
    TenantInfoTermOfLeaseFrom = scrapy.Field()
    TenantInfoTermOfLeaseTo = scrapy.Field()
    AgencyContacts = scrapy.Field()
    AgencyID = scrapy.Field()
    IsYoutube = scrapy.Field()
    Height = scrapy.Field()
    Width = scrapy.Field()
    YoutubeId = scrapy.Field()
    VideoRequired = scrapy.Field()
    VideoSrc = scrapy.Field()
    Autoplay = scrapy.Field()
    ListingInspectionKnowledgeGraph = scrapy.Field()
    ImageNumber_0_url = scrapy.Field()
    ImageNumber_0_url_transformed = scrapy.Field()
    ImageNumber_1_url = scrapy.Field()
    ImageNumber_1_url_transformed = scrapy.Field()
    ImageNumber_2_url = scrapy.Field()
    ImageNumber_2_url_transformed = scrapy.Field()
    ImageNumber_3_url = scrapy.Field()
    ImageNumber_3_url_transformed = scrapy.Field()
    ImageNumber_4_url = scrapy.Field()
    ImageNumber_4_url_transformed = scrapy.Field()
    ImageNumber_5_url = scrapy.Field()
    ImageNumber_5_url_transformed = scrapy.Field()
    ImageNumber_6_url = scrapy.Field()
    ImageNumber_6_url_transformed = scrapy.Field()
    ImageNumber_7_url = scrapy.Field()
    ImageNumber_7_url_transformed = scrapy.Field()
    ImageNumber_8_url = scrapy.Field()
    ImageNumber_8_url_transformed = scrapy.Field()
    ImageNumber_9_url = scrapy.Field()
    ImageNumber_9_url_transformed = scrapy.Field()
    ImageNumber_10_url = scrapy.Field()
    ImageNumber_10_url_transformed = scrapy.Field()
    ImageNumber_11_url = scrapy.Field()
    ImageNumber_11_url_transformed = scrapy.Field()
    ImageNumber_12_url = scrapy.Field()
    ImageNumber_12_url_transformed = scrapy.Field()
    ImageNumber_13_url = scrapy.Field()
    ImageNumber_13_url_transformed = scrapy.Field()
    ImageNumber_14_url = scrapy.Field()
    ImageNumber_14_url_transformed = scrapy.Field()
    ImageNumber_15_url = scrapy.Field()
    ImageNumber_15_url_transformed = scrapy.Field()
    ImageNumber_16_url = scrapy.Field()
    ImageNumber_16_url_transformed = scrapy.Field()
    ImageNumber_17_url = scrapy.Field()
    ImageNumber_17_url_transformed = scrapy.Field()
    ImageNumber_18_url = scrapy.Field()
    ImageNumber_18_url_transformed = scrapy.Field()
    ImageNumber_19_url = scrapy.Field()
    ImageNumber_19_url_transformed = scrapy.Field()
    ImageNumber_20_url = scrapy.Field()
    ImageNumber_20_url_transformed = scrapy.Field()
    ImageNumber_21_url = scrapy.Field()
    ImageNumber_21_url_transformed = scrapy.Field()
    ImageNumber_22_url = scrapy.Field()
    ImageNumber_22_url_transformed = scrapy.Field()
    ImageNumber_23_url = scrapy.Field()
    ImageNumber_23_url_transformed = scrapy.Field()
    ImageNumber_24_url = scrapy.Field()
    ImageNumber_24_url_transformed = scrapy.Field()
    ImageNumber_25_url = scrapy.Field()
    ImageNumber_25_url_transformed = scrapy.Field()
    ImageNumber_26_url = scrapy.Field()
    ImageNumber_26_url_transformed = scrapy.Field()
    ImageNumber_27_url = scrapy.Field()
    ImageNumber_27_url_transformed = scrapy.Field()
    ImageNumber_28_url = scrapy.Field()
    ImageNumber_28_url_transformed = scrapy.Field()
    ImageNumber_29_url = scrapy.Field()
    ImageNumber_29_url_transformed = scrapy.Field()
    Agent_0_Fax = scrapy.Field()
    Agent_0_MugshotUrl = scrapy.Field()
    Agent_0_Mobile = scrapy.Field()
    Agent_0_Telephone = scrapy.Field()
    Agent_0_Address = scrapy.Field()
    Agent_0_FullName = scrapy.Field()
    Agent_1_Fax = scrapy.Field()
    Agent_1_MugshotUrl = scrapy.Field()
    Agent_1_Mobile = scrapy.Field()
    Agent_1_Telephone = scrapy.Field()
    Agent_1_Address = scrapy.Field()
    Agent_1_FullName = scrapy.Field()
    Agent_2_Fax = scrapy.Field()
    Agent_2_MugshotUrl = scrapy.Field()
    Agent_2_Mobile = scrapy.Field()
    Agent_2_Telephone = scrapy.Field()
    Agent_2_Address = scrapy.Field()
    Agent_2_FullName = scrapy.Field()
    Agent_3_Fax = scrapy.Field()
    Agent_3_MugshotUrl = scrapy.Field()
    Agent_3_Mobile = scrapy.Field()
    Agent_3_Telephone = scrapy.Field()
    Agent_3_Address = scrapy.Field()
    Agent_3_FullName = scrapy.Field()
    Agent_4_Fax = scrapy.Field()
    Agent_4_MugshotUrl = scrapy.Field()
    Agent_4_Mobile = scrapy.Field()
    Agent_4_Telephone = scrapy.Field()
    Agent_4_Address = scrapy.Field()
    Agent_4_FullName = scrapy.Field()
    Agent_5_Fax = scrapy.Field()
    Agent_5_MugshotUrl = scrapy.Field()
    Agent_5_Mobile = scrapy.Field()
    Agent_5_Telephone = scrapy.Field()
    Agent_5_Address = scrapy.Field()
    Agent_5_FullName = scrapy.Field()
    Agent_6_Fax = scrapy.Field()
    Agent_6_MugshotUrl = scrapy.Field()
    Agent_6_Mobile = scrapy.Field()
    Agent_6_Telephone = scrapy.Field()
    Agent_6_Address = scrapy.Field()
    Agent_6_FullName = scrapy.Field()
    Agent_7_Fax = scrapy.Field()
    Agent_7_MugshotUrl = scrapy.Field()
    Agent_7_Mobile = scrapy.Field()
    Agent_7_Telephone = scrapy.Field()
    Agent_7_Address = scrapy.Field()
    Agent_7_FullName = scrapy.Field()
    Agent_8_Fax = scrapy.Field()
    Agent_8_MugshotUrl = scrapy.Field()
    Agent_8_Mobile = scrapy.Field()
    Agent_8_Telephone = scrapy.Field()
    Agent_8_Address = scrapy.Field()
    Agent_8_FullName = scrapy.Field()
    Agent_9_Fax = scrapy.Field()
    Agent_9_MugshotUrl = scrapy.Field()
    Agent_9_Mobile = scrapy.Field()
    Agent_9_Telephone = scrapy.Field()
    Agent_9_Address = scrapy.Field()
    Agent_9_FullName = scrapy.Field()
    Agent_10_Fax = scrapy.Field()
    Agent_10_MugshotUrl = scrapy.Field()
    Agent_10_Mobile = scrapy.Field()
    Agent_10_Telephone = scrapy.Field()
    Agent_10_Address = scrapy.Field()
    Agent_10_FullName = scrapy.Field()
    Agent_11_Fax = scrapy.Field()
    Agent_11_MugshotUrl = scrapy.Field()
    Agent_11_Mobile = scrapy.Field()
    Agent_11_Telephone = scrapy.Field()
    Agent_11_Address = scrapy.Field()
    Agent_11_FullName = scrapy.Field()
    Agent_12_Fax = scrapy.Field()
    Agent_12_MugshotUrl = scrapy.Field()
    Agent_12_Mobile = scrapy.Field()
    Agent_12_Telephone = scrapy.Field()
    Agent_12_Address = scrapy.Field()
    Agent_12_FullName = scrapy.Field()
    Agent_13_Fax = scrapy.Field()
    Agent_13_MugshotUrl = scrapy.Field()
    Agent_13_Mobile = scrapy.Field()
    Agent_13_Telephone = scrapy.Field()
    Agent_13_Address = scrapy.Field()
    Agent_13_FullName = scrapy.Field()
    Agent_14_Fax = scrapy.Field()
    Agent_14_MugshotUrl = scrapy.Field()
    Agent_14_Mobile = scrapy.Field()
    Agent_14_Telephone = scrapy.Field()
    Agent_14_Address = scrapy.Field()
    Agent_14_FullName = scrapy.Field()
    Agent_15_Fax = scrapy.Field()
    Agent_15_MugshotUrl = scrapy.Field()
    Agent_15_Mobile = scrapy.Field()
    Agent_15_Telephone = scrapy.Field()
    Agent_15_Address = scrapy.Field()
    Agent_15_FullName = scrapy.Field()
    Agent_16_Fax = scrapy.Field()
    Agent_16_MugshotUrl = scrapy.Field()
    Agent_16_Mobile = scrapy.Field()
    Agent_16_Telephone = scrapy.Field()
    Agent_16_Address = scrapy.Field()
    Agent_16_FullName = scrapy.Field()
    Agent_17_Fax = scrapy.Field()
    Agent_17_MugshotUrl = scrapy.Field()
    Agent_17_Mobile = scrapy.Field()
    Agent_17_Telephone = scrapy.Field()
    Agent_17_Address = scrapy.Field()
    Agent_17_FullName = scrapy.Field()
    Agent_18_Fax = scrapy.Field()
    Agent_18_MugshotUrl = scrapy.Field()
    Agent_18_Mobile = scrapy.Field()
    Agent_18_Telephone = scrapy.Field()
    Agent_18_Address = scrapy.Field()
    Agent_18_FullName = scrapy.Field()
    Agent_19_Fax = scrapy.Field()
    Agent_19_MugshotUrl = scrapy.Field()
    Agent_19_Mobile = scrapy.Field()
    Agent_19_Telephone = scrapy.Field()
    Agent_19_Address = scrapy.Field()
    Agent_19_FullName = scrapy.Field()
    PriceDecimal  = scrapy.Field()
    BuildAreaDecimal = scrapy.Field()
    LandAreaDecimal = scrapy.Field()
    