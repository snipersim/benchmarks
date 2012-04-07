#include <stdio.h>

#include "sim_api.h"
#include "hooks_base.h"

void parmacs_roi_begin() {
  printf("[HOOKS] Entering ROI\n"); fflush(NULL);
  SimRoiStart();
}

void parmacs_roi_end() {
  SimRoiEnd();
  printf("[HOOKS] Leaving ROI\n"); fflush(NULL);
}
