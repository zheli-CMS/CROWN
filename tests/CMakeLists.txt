# Add target to download input file
add_test(NAME download_sample
    WORKING_DIRECTORY ${INSTALLDIR}
    COMMAND curl -OL https://github.com/KIT-CMS/CROWNTestingSamples/raw/main/nanoAOD.root)
set_tests_properties(download_sample PROPERTIES FIXTURES_SETUP download_sample)

# Generate a test for each generated target
foreach(TARGET_NAME ${TARGET_NAMES})
    message(STATUS "Add test for target ${TARGET_NAME}")
    add_test(NAME ${TARGET_NAME}
             WORKING_DIRECTORY ${INSTALLDIR}
             COMMAND ${TARGET_NAME} output_${TARGET_NAME}.root nanoAOD.root)
    set_tests_properties(${TARGET_NAME} PROPERTIES FIXTURES_REQUIRED download_sample)
endforeach()