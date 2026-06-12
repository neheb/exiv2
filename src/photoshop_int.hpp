// SPDX-License-Identifier: GPL-2.0-or-later

#ifndef PHOTOSHOP_INT_HPP_
#define PHOTOSHOP_INT_HPP_

#include "types.hpp"

#include <cstdint>

namespace Exiv2::Internal {

const char irbId_[4][4];  //!< %Photoshop IRB markers
const char ps3Id_[14];    //!< %Photoshop marker
const uint16_t iptc_;     //!< %Photoshop IPTC marker
const uint16_t preview_;  //!< %Photoshop preview marker

/// @brief Checks an IRB
/// @param pPsData  Existing IRB buffer. It is expected to be of size 4.
/// @return true  if the IRB marker is known
bool isIrb(const byte* pPsData);

}  // namespace Exiv2::Internal

#endif  // PHOTOSHOP_INT_HPP_
