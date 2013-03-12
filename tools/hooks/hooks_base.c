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

void parmacs_setup(void) __attribute ((constructor));
void parmacs_setup(void) {
#if defined(PARMACS_NO_ROI)
  parmacs_roi_begin();
#endif
}

void parmacs_shutdown(void) __attribute ((destructor));
void parmacs_shutdown(void) {
#if defined(PARMACS_NO_ROI)
  parmacs_roi_end();
#endif
}
